from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_aws import BedrockEmbeddings, ChatBedrockConverse
from langchain_community.vectorstores import FAISS


def build_vector_store():
    loader = PyPDFLoader("data/pdf/Leave-Policy-India.pdf")
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_documents(documents)

    embeddings = BedrockEmbeddings(
        credentials_profile_name="default",
        model_id="amazon.titan-embed-text-v2:0"
    )

    vector_store = FAISS.from_documents(chunks, embeddings)
    return vector_store


def hr_llm():
    llm = ChatBedrockConverse(
        credentials_profile_name="default",
        model_id="deepseek.v3.2",
        temperature=0.1,
        max_tokens=3000,
        top_p=0.9
    )
    return llm


def hr_rag_response(question):
    vector_store = build_vector_store()
    rag_llm = hr_llm()

    relevant_docs = vector_store.similarity_search(question, k=3)
    context = "\n\n".join([doc.page_content for doc in relevant_docs])

    prompt = f"""
You are an HR policy assistant. Answer the user's question using only the context below.

Context:
{context}

Question:
{question}

Answer:
"""

    response = rag_llm.invoke(prompt)
    return response.content
