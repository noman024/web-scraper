# api/routes.py
from fastapi import APIRouter
from extraction.extractor import extract_data

router = APIRouter()

@router.post("/extract")
async def extract_data_from_webpage(url: str, schema: dict) -> dict:
    """
    Extract structured data from a webpage based on the provided URL and schema.

    Args:
        url (str): The URL of the webpage to extract data from.
        schema (dict): The schema defining the structure of the data to extract.

    Returns:
        dict: The extracted data.

    This function uses the extract_data function from the extraction.extractor module
    to perform the extraction. The extracted data is returned as a dictionary.
    """
    
    # Call the extract_data function to extract data from the webpage
    extracted_data = extract_data(url, schema)
    
    # Return the extracted data
    return extracted_data
