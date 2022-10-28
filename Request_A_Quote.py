import streamlit as st
from deta import Deta

st.image('./LOGO_091622.png')
st.header('Request A Quote For Property Management & Financial Analysis.')
st.subheader('Please answer the following questions and submit your request below.')

# Data to be written to Deta Base
with st.form("form"):
    name = st.text_input("Name of Building:")
    address = st.text_input("Building Address:")
    typeof = st.text_input("Type of Community, HOA, COA, APT?")
    budget = st.number_input("Current Annual Budget Amount?")
    qone = st.text_input("Current Building Violations?")
    qtwo = st.text_input("Current Ongoing Projects?")
    qthree = st.text_input("Provide any questions or cocncerns here:")
    
    submitted = st.form_submit_button("Submit your quote request.")
    clear_on_submit=True   
    
# Insert a file uploader that accepts multiple files at a time
uploaded_files = st.file_uploader("Provide a copy of budget, violation letter(s), etc. here", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)                

# Financial analysis


# Connect to Deta Base with your Project Key
deta = Deta(st.secrets["deta_key"])
db = deta.Base("Request_A_Quote_App")

# If the user clicked the submit button
# write the data from the form to the database.
# You can store any data you want here. Just modify that dictionary below (the entries between the {}).
if submitted:
    db.put({"name": name, "address": address, "typeof": typeof, "budget": budget, 
            "q1": qone, "q2": qtwo, "q3": qthree})
    if submitted:
        st.write("Your answers have been successfully sent. For any questions or concerns please contact the office @ equin@assetmana.com or 305.209.5235. Please close your browser when you are finished.")
"---"
# This reads all items from the database and displays them to your app.
# db_content is a list of dictionaries. You can do everything you want with it.
db_content = db.fetch(query=None, limit=None, last=None).items

