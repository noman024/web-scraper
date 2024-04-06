# extraction/extractor.py
from bs4 import BeautifulSoup
import requests

def extract_data(url: str, schema: dict):
    """
    Extracting structured data from a webpage based on the provided URL and schema.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        webpage_content = response.content

        # Parsing HTML content
        soup = BeautifulSoup(webpage_content, 'html.parser')
        # print(soup)

        # Extracting data based on schema
        extracted_data = {}
        
        # Checking if "attributes" key exists in the schema
        if "attributes" in schema:
            print("Attributes found in schema")
        else:
            print("Attributes key not found in schema")

        # Iterating over each attribute in the schema
        for attribute in schema.get("attributes", []):
            # print(f"Processing attribute: {attribute}")
            name = attribute.get("name")
            selector = attribute.get("selector")
            # print(f"Attribute name: {name}, Selector: {selector}")
            
            # Selecting elements based on the provided selector
            elements = soup.select(selector)
            # print(f"Selected elements: {elements}")

            # Extracting text content from selected elements
            extracted_values = [element.text.strip() for element in elements]
            # print(f"Extracted values: {extracted_values}")

            # Storing extracted values under the attribute name
            extracted_data[name] = extracted_values
        
        return extracted_data

    except Exception as e:
        return {"error": str(e)}
