import streamlit as st
import chatbot_backend as demo

st.set_page_config(
    page_title="NomadIQ Enterprise HR RAG Assistant",
    page_icon="🤖",
    layout="wide"
)

# =========================
# Sidebar
# =========================
with st.sidebar:
    st.image("assets/nomadtec_logo.png", width=230)

    st.markdown("## Enterprise HR RAG Assistant")
    st.write(
        "A GenAI-powered HR knowledge assistant using "
        "Retrieval-Augmented Generation (RAG)."
    )

    st.divider()

    st.markdown("### Technology Stack")
    st.markdown("""
**AWS AI Services**
- Amazon Bedrock
- Titan Embeddings V2
- DeepSeek v3.2

**Vector Search**
- FAISS

**Frameworks**
- LangChain
- Streamlit
""")

    st.divider()

    st.markdown("### Status")
    st.write("Production Prototype")
    st.write("Version: v1.0.0")

    st.divider()

    st.markdown("### Built By")
    st.write("Larry Dana Gaither")
    st.caption("NomadTec | Enterprise AI Transformation")

# =========================
# Main Page
# =========================

st.title("📚 NomadIQ Enterprise HR Knowledge Assistant")

st.write(
    "Ask natural-language questions about the HR Leave Policy document. "
    "Responses are generated using Retrieval-Augmented Generation (RAG) "
    "with Amazon Bedrock."
)

st.markdown("## Example Questions")

col1, col2 = st.columns(2)

with col1:
    st.info("What types of leave are available?")

with col2:
    st.info("Explain the difference between Casual Leave and Sick Leave.")

st.divider()

question = st.text_area(
    "Ask your HR policy question",
    placeholder="Example: What types of leave are available?"
)

if st.button("🚀 Ask NomadIQ", type="primary"):

    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Searching HR policy and generating response..."):
            answer = demo.hr_rag_response(question)

        st.markdown("## Answer")
        st.success(answer)

st.divider()

st.caption(
    "Prototype built using Amazon Bedrock, Titan Embeddings V2, DeepSeek v3.2, "
    "FAISS, LangChain, and Streamlit."
)