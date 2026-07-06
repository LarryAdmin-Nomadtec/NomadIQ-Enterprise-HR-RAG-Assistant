import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_aws import BedrockEmbeddings, ChatBedrockConverse
from langchain_community.vectorstores import FAISS

data_load = PyPDFLoader("data/pdf/Leave-Policy-India.pdf")
data_test = data_load.load()
print(len(data_test))
print(data_test[0])

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
docs = text_splitter.split_documents(data_test)

print(len(docs))
embeddings = BedrockEmbeddings(
    credentials_profile_name="default",
    model_id="amazon.titan-embed-text-v2:0"
)
print("Embeddings client created")