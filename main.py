import json
import openai
import easyocr
from dataclasses import dataclass, asdict
from typing import List, Optional
from rich import print

openai.api_key = "xxx"


@dataclass
class OCRResult:
    """
    Data class to store OCR results
    """
    firstName: str
    lastName: str
    citizenship: str
    documentNumber: str
    dateOfBirth: str


def load_model() -> easyocr.Reader:
    """
    Load OCR model into memory.
    """
    reader = easyocr.Reader(["ru", "rs_cyrillic", "be", "bg", "uk", "mn", "en"])
    return reader


def read_text(reader: easyocr.Reader, image_path: str) -> List[str]:
    """
    Read text from image using OCR.
    """
    result = reader.readtext(image_path)
    return [data[1] for data in result]


def create_prompt(text_data: List[str]) -> str:
    """
    Create a prompt for OpenAI model.
    """
    prompt = f"""
    Replace the values from this example json and remember, the first letter of names should be capitalized, 
    the citizenship should be a 3-letter country code, the date should be in the format mm.dd.yyyy and only contain 2 dots:
        {{
        "firstName": "",
        "lastName": ""
        "citizenship": "",
        "documentNumber": "",
        "dateOfBirth": ""
        }}
    with this data:
    {str(text_data)}
    """
    return prompt


def get_completion(prompt: str) -> Optional[str]:
    """
    Get completion from OpenAI model.
    """
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": prompt},
        ]
    )
    response = completion.get('choices', [{}])[0].get('message', {}).get('content', None)
    
    response_dict = json.loads(response)
    result = OCRResult(**response_dict)
    return asdict(result)


def main():
    image_path = "/Users/User/Downloads/osobna.jpg"
    
    # Load model
    reader = load_model()
    # Read text
    text_data = read_text(reader, image_path)
    # Create prompt
    prompt = create_prompt(text_data)
    # Get completion
    response = get_completion(prompt)

    print(response) 


if __name__ == "__main__":
    main()
