import streamlit as st
import requests
import uuid

WORQHAT_API_KEY = 'your API Key here'
API_ENDPOINT_URL = 'https://api.worqhat.com/api/ai/content/v4'


# Function to send files and/or text to the API
def send_files_text(question, files=None, training_data=None, first_message=False):
    headers = {'Authorization': 'Bearer ' + WORQHAT_API_KEY}
    data = {
        'question': question,
        'training_data': training_data,
        'model': 'aicon-v4-nano-160824',
        'conversation_id': st.session_state.conversation_id,
    }

    if first_message and files:
        files_to_send = [('files', (file.name, file, file.type)) for file in files]
        response = requests.post(API_ENDPOINT_URL, headers=headers, files=files_to_send, data=data)
    else:
        headers['Content-Type'] = 'application/json'
        response = requests.post(API_ENDPOINT_URL, headers=headers, json=data)

    if response.status_code == 200:
        response_data = response.json()
        content = response_data.get('content', '')
        if content:
            st.session_state.chat_history.append({'sender': 'Bot', 'message': content})
        else:
            st.error(f'Error: No content received. {response.status_code}, {response.text}')
    else:
        st.error(f'Error: {response.status_code}, {response.text}')


# Create the conversation id
if 'conversation_id' not in st.session_state:
    st.session_state.conversation_id = str(uuid.uuid4())

# Display the conversation ID
st.write(f"Conversation ID: {st.session_state.conversation_id}")

# File uploader sidebar
uploaded_files = st.sidebar.file_uploader("Choose a file", type=["png", "jpg", "jpeg", "pdf"],
                                          accept_multiple_files=True)

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'first_message_sent' not in st.session_state:
    st.session_state.first_message_sent = False

# Chat Interface
user_input = st.chat_input("Ask a question", key="chat_input")
if user_input:
    st.session_state.chat_history.append({'sender': 'User', 'message': user_input})

    # Send the files and question only on the first message if files are uploaded
    if uploaded_files and not st.session_state.first_message_sent:
        send_files_text(question=user_input, files=uploaded_files, first_message=True)
        st.session_state.first_message_sent = True
    else:
        send_files_text(question=user_input, first_message=False)

    # Display the chat history
    for chat in st.session_state.chat_history:
        with st.chat_message(chat['sender']):
            st.write(chat['message'])
