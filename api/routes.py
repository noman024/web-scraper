# api/routes.py
from fastapi import APIRouter
from extraction.extractor import extract_data

router = APIRouter()


@router.post("/extract")
async def extract_data_from_webpage(url: str, schema: dict):
    """
    Extracting structured data from a webpage based on the provided URL and schema.
    """
    extracted_data = extract_data(url, schema)
    # print("routes.py executed!!!")
    return extracted_data
