import streamlit as st
import requests
import json
import re

# Ollama API URL
OLLAMA_URL = "http://localhost:11434/api/generate"

st.set_page_config(page_title="DeepSeek Chat", page_icon="🤖")

st.title("🤖 DeepSeek @Mahathir's PC")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if user_input := st.chat_input("Type your message..."):
    # Display user message
    st.chat_message("user").markdown(user_input)
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # Prepare request payload
    payload = {
        "model": "deepseek-r1:1.5b",
        "prompt": user_input,
        "stream": True
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, stream=True, timeout=60)
        response.raise_for_status()  # Raise an error for bad responses

        # Initialize variable to accumulate AI response
        ai_response = ""

        # Create a placeholder for the assistant's message
        assistant_placeholder = st.empty()

        # Process each chunk in the stream
        for chunk in response.iter_lines():
            if chunk:
                data = chunk.decode('utf-8')
                result = json.loads(data)

                # Get the response and remove all <think> tags
                chunk_response = result.get("response", "")
                chunk_response_cleaned = re.sub(r"<think>.*?</think>", "", chunk_response)  # Remove <think> tags
                chunk_response_cleaned = re.sub(r"\s{2,}", " ", chunk_response_cleaned)  # Replace multiple spaces with a single space
                
                ai_response += chunk_response_cleaned

                # Display the AI response incrementally
                with assistant_placeholder.chat_message("assistant"):
                    st.markdown(ai_response)

        # Update the session state with the final response
        st.session_state["messages"].append({"role": "assistant", "content": ai_response})

    except requests.exceptions.RequestException as e:
        st.error(f"Error communicating with Ollama API: {e}")