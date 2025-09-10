import streamlit as st
import random
import time
import utils

st.title("AI Integrated Job Interview Preparation (AI Chatbot) ")
st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
st.divider()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi, I am your virtual AI Interviewer. Please introduce yourself"}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        assistant_response = random.choice(
            [
                "Describe a time you resolved a difficult customer issue.",
                "How did you ensure food safety in your previous role?",
                "Give an example of successful teamwork during a busy period.",
                "How would you handle conflicting customer orders?",
                "How will your e-commerce training help you in this role?",
                "How do you stay organized in a fast-paced environment?",
                "Describe a time you went above and beyond for a customer.",
                "How do you handle repetitive tasks?",
                "What motivates you to provide excellent customer service?",
                "How do you stay updated on food safety regulations?",
            ]
        )
        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
