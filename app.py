import streamlit as st
import chatbot_backend as demo

st.set_page_config(page_title="NomadIQ HR Knowledge Assistant with RAG")

new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">NomadIQ HR Knowledge Assistant with RAG 🎯</p>'
st.markdown(new_title, unsafe_allow_html=True)

st.write("Ask a question about the HR leave policy document.")

input_text = st.text_area("Enter your HR policy question here")

go_button = st.button("📌 Ask NomadIQ", type="primary")

if go_button:
    if input_text.strip() == "":
        st.warning("Please enter a question first.")
    else:
        with st.spinner("Retrieving relevant HR policy context and generating an answer..."):
            response_content = demo.hr_rag_response(input_text)
            st.write(response_content)