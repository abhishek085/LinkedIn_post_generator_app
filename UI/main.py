import streamlit as st


# Set up the app title
st.title("LLM Post Generator")

# Create three dropdowns for categories
category1 = st.selectbox("Category 1", ["Technology", "Health", "Education", "Finance", "Entertainment"])
category2 = st.selectbox("Category 2", ["AI", "Nutrition", "Online Learning", "Investing", "Movies"])
category3 = st.selectbox("Category 3", ["Machine Learning", "Exercise", "E-learning Platforms", "Cryptocurrency", "TV Shows"])

# Create a text input box
post_topic = st.text_input("Enter the topic for the post:")

# Create a submit button
if st.button("Generate Post"):
    # Placeholder for the generated post
    result = f"Generating a post for the topic: '{post_topic}' under categories: {category1}, {category2}, {category3}."
    
    # Display the result
    st.text_area("Generated Post", result)
