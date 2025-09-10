import streamlit as st
import utils
import tempfile
import os

# Define the folder where the uploaded PDF will be saved
save_dir = './uploads/'

#print(save_dir)

# Create the directory if it doesn't exist
os.makedirs(save_dir, exist_ok=True)

st.title("AI Integrated Resume Skills & Competencies Extraction and Analysis (PDF) ")
st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
st.divider()

col_input , col_rag = st.columns([1,4])
with col_input:
    selected_file = st.file_uploader("PDF File", type=["pdf"])

    if selected_file is not None:
        data = selected_file.getvalue()
        # Construct the full path for the saved file
        file_path = os.path.join(save_dir, selected_file.name)

        try:
            with st.spinner("Writing file..."):
                # Write the uploaded file's content to the path
                with open(file_path, "wb") as f:
                    written = f.write(selected_file.getvalue())

                if written == len(data):
                    # st.write(f"File saved to: {file_path}")
                    st.success("File uploaded successfully!")
                else:
                    st.warning("Partial write: Not all data may have been saved.")
                # Now you can use 'file_path' for further processing

        except Exception as e:
            st.error(f"File write failed: {e}")
    
#    if selected_file is not None:
        # Create a temporary directory
#        with tempfile.TemporaryDirectory() as temp_dir:
            # Construct the full path for the saved file
#            file_path = os.path.join(temp_dir, selected_file.name)

            # Write the uploaded file's content to the temporary path
#            with open(file_path, "wb") as f:
#                f.write(selected_file.getvalue())

#            st.write(f"File saved to temporary path: {file_path}")
            # Now you can use 'file_path' for further processing
    
    st.divider()
    prompt = st.text_input("Prompt",key="pdf_prompt")
    st.divider()
    sumbit_btn = st.button(label="Submit",key="pdf_btn")

if sumbit_btn:
    with col_rag:
        with st.spinner("Processing..."):
            st.success("Response: Answering with RAG...")
            # response,relevant_documents = utils.rag_with_pdf(file_path=f"./data/{selected_file.name}",
            #                                                      prompt=prompt)
            print(file_path)
            response,relevant_documents = utils.rag_with_pdf(file_path=file_path,prompt=prompt)
            st.markdown(response)
            st.divider()
            st.info("Documents")
            for doc in relevant_documents:
                st.caption(doc.page_content)
                st.markdown(f"Source: {doc.metadata}")
                st.divider()

            # with col_normal:
            #    with st.spinner("Processing..."):
            #        st.info("Response: Answering without RAG...")
            #        response = utils.ask_gemini(prompt)
            #        st.markdown(response)
            #        st.divider()
            