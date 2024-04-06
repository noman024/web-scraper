import streamlit as st
from api.routes import extract_data

def main():
    """
    Main function of the Streamlit app. Displays a title, allows the user to input a URL and keywords,
    and extracts data from a webpage using the provided URL and keywords.
    """

    # Display the title of the app
    st.title("Web Scraping Application")

    # Ask the user to input a URL
    url = st.text_input("Enter URL:")

    # Ask the user how many keywords they want to input and dynamically generate input fields for keywords
    num_keywords = st.number_input(
        "Number of Keywords:",
        min_value=1,
        max_value=10,
        value=1,
        step=1
    )
    keywords = []
    for i in range(num_keywords):
        keyword = st.text_input(f"Enter Keyword {i+1}:")
        keywords.append(keyword)

    # If the user clicks the "Extract Data" button, extract data from the webpage
    if st.button("Extract Data"):
        try:
            # Construct a schema using the provided keywords
            schema = {
                "attributes": [
                    {"name": keyword, "selector": keyword}
                    for keyword in keywords
                ]
            }

            # Extract data from the webpage using the provided URL and schema
            extracted_data = extract_data(url, schema)

            # Display the extracted data
            st.write("Extracted Data:")
            st.write(extracted_data)

        # If there is an error, display the error message
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
