# extraction/extractor.py
from bs4 import BeautifulSoup
import requests

def extract_data(url: str, schema: dict) -> dict:
    """
    Extracts structured data from a webpage based on the provided URL and schema.

    Args:
        url (str): The URL of the webpage to extract data from.
        schema (dict): The schema defining the structure of the data to extract.

    Returns:
        dict: The extracted data.

    Raises:
        Exception: If any error occurs during the extraction process.

    This function uses the BeautifulSoup library to parse the HTML content of the webpage.
    It then iterates over each attribute defined in the schema, selects elements based on the
    provided selector, extracts the text content from those elements, and stores the extracted
    values under the attribute name in the extracted_data dictionary.
    """
    try:
        # Make a GET request to the provided URL
        response = requests.get(url)
        response.raise_for_status()

        # Get the HTML content of the webpage
        webpage_content = response.content

        # Parse the HTML content
        soup = BeautifulSoup(webpage_content, 'html.parser')

        # Initialize the dictionary to store extracted data
        extracted_data = {}

        # Check if the schema has attributes defined
        if "attributes" in schema:
            print("Attributes found in schema")
        else:
            print("Attributes key not found in schema")

        # Iterate over each attribute in the schema
        for attribute in schema.get("attributes", []):
            # Get the name and selector of the attribute
            name = attribute.get("name")
            selector = attribute.get("selector")

            # Select elements based on the provided selector
            elements = soup.select(selector)

            # Extract text content from selected elements
            extracted_values = [element.text.strip() for element in elements]

            # Store extracted values under the attribute name
            extracted_data[name] = extracted_values

        return extracted_data

    except Exception as e:
        # Return an error dictionary if any exception occurs
        return {"error": str(e)}
