import streamlit as st
from api.routes import extract_data

def main():
    st.title("Web Scraping Application")

    # User input for URL
    url = st.text_input("Enter URL:")

    # Dynamic input for keywords
    num_keywords = st.number_input("Number of Keywords:", min_value=1, max_value=10, value=1, step=1)
    keywords = []
    for i in range(num_keywords):
        keyword = st.text_input(f"Enter Keyword {i+1}:")
        keywords.append(keyword)

    # Button to trigger data extraction
    if st.button("Extract Data"):
        try:
            # Construct schema from dynamically provided keywords
            schema = {"attributes": [{"name": keyword, "selector": keyword} for keyword in keywords]}

            # Call extract_data function
            extracted_data = extract_data(url, schema)

            # Display extracted data
            st.write("Extracted Data:")
            st.write(extracted_data)

        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
