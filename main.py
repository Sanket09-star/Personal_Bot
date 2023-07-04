import streamlit as st
from streamlit_chat import message
from bardapi import Bard

# function ton generate output
'''
For token :
Go to the google bard 
Sign in your account 
Then go to inspect section
Click on application then cookies
then click on first link(https:bard.google...
find in the 'Name' column '_Secure-1PSID' in that row copy Value of that _Secure-1PSID
Paste that value in token..

Note : while performing this application you must signed in google bard
Your token value is important, Therefore do not share your token value.

It is better to  use JSON string as the credential for Client initialization instead of the filepath.
'''


def generate_response(prompt):
    token = 'XXXXXX'
    bard = Bard(token=token)
    response = bard.get_answer(prompt)['content']
    return response

# function to recive user quires


def get_text():
    input_text = st.text_input("BOT:", "Hello !!", key="input")
    return input_text


# Tile of the stramlit app
st.title('Personal Bot')


# fun to add background image
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/free-vector/tropical-leaves-background-zoom_23-2148580778.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
        
         """,
         unsafe_allow_html=True
     )


add_bg_from_url()


print(st.session_state)
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

# Accepting user input
user_input = get_text()
if user_input:
    print(user_input)
    output = generate_response(user_input)
    print(output)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

# Displaying generated answer
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['generated'][i], key=str(i))
        message(st.session_state['past'][i], key="user_"+str(i), is_user=True)
