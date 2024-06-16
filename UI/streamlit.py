import streamlit as st
from app import create_post
# LinkedIn blue color and background color
linkedin_blue = "#0077b5"
background_color = "#F7DAAD"

# Set up the app title
st.markdown(f"<h1 style='color:{linkedin_blue}; text-align: center;'>LinkedIn Post Generator</h1>", unsafe_allow_html=True)

# Apply custom CSS for styling and background color
st.markdown(
    f"""
    <style>
    body {{
        background-color: {background_color};
    }}
    .stSelectbox label, .stTextInput label {{
        color: {linkedin_blue};
    }}
    .stButton button {{
        background-color: {linkedin_blue};
        color: white;
        border-radius: 4px;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }}
    .stButton button:hover {{
        background-color: #005f8d;
    }}
    .stTextArea label {{
        color: {linkedin_blue};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Create three dropdowns for categories
post_type = st.selectbox("Post Type", ["Though and Leadership piece", "Industry update", "Job Posting", "Annoucement"])
ts = st.selectbox("Tone and Style", ["Professional", "Casual", "Informative", "Advertisement", "Insights"])
length = st.selectbox("Length", ["Short", "Medium", "Long"])

# Create a text input box
context = st.text_input("Enter the topic for the post:")

# Create a submit button
if st.button("Generate Post"):
    # Placeholder for the generated post
    result = create_post(post_type=post_type,ts=ts,length=length,context=context)
    # result = f"Generating a post for the topic: '{post_topic}' under categories: {category1}, {category2}, {category3}."
    
    # Display the result
    st.text_area("Generated Post", result)
