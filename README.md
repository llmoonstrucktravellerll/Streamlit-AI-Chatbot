# Streamlit-AI-Chatbot
Streamlit AI Chatbot with File Upload Support is a versatile application built using Streamlit that enables users to interact with an AI model through a chat interface.


Code Overview:
This code is a Streamlit-based AI chatbot interface that allows users to ask questions and upload files. It sends the input to the Worqhat API and displays the responses. The chatbot can handle conversations and file uploads, maintaining a chat history within the Streamlit session.

Description:
Abstract: A Streamlit application that interacts with the Worqhat AI API to provide a chat interface where users can ask questions and upload files. The app maintains a conversation ID and chat history for ongoing interactions.

Steps:

Initialize the Streamlit app and generate a unique conversation ID.
Handle file uploads via the sidebar.
Send user input and uploaded files to the Worqhat API.
Display chat history in the app interface.
Key Methods:

send_files_text(): Sends user input and files to the API and handles the response.
Streamlit components: st.chat_input, st.chat_message, st.file_uploader, st.write for UI interactions.
Important Commands:

Run Streamlit App:
bash
Copy code
streamlit run main.py
Set API Key as Environment Variable (before running the app):
bash
Copy code
export WORQHAT_API_KEY='your-api-key-here'
This code allows for dynamic interactions between a user and the AI, with the ability to upload files and maintain a conversation flow.

result:
![image](https://github.com/user-attachments/assets/8837fadc-9d34-4518-96d1-f3c2d285ac01)

