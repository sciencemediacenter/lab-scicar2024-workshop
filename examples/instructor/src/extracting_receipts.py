# cf. https://python.useinstructor.com/examples/extracting_receipts/

import instructor
from pydantic import BaseModel, model_validator
from openai import OpenAI
import os
from devtools import pprint

class Item(BaseModel):
    name: str
    price: float
    quantity: int

class Receipt(BaseModel):
    items: list[Item]
    total: float

@model_validator(mode="after")
def check_total(cls, values: "Receipt"):
    items = values.items
    total = values.total
    calculated_total = sum(item.price * item.quantity for item in items)
    if calculated_total != total:
        raise ValueError(
            f"Total {total} does not match the sum of item prices {calculated_total}"
        )
    return values


client = instructor.from_openai(
    client=OpenAI(api_key=os.getenv("OPENAI_API_KEY")),
    mode=instructor.Mode.TOOLS,
)

def extract(url: str) -> Receipt:
    return client.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=4000,
        response_model=Receipt,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {"url": url},
                    },
                    {
                        "type": "text",
                        "text": "Analyze the image and return the items in the receipt and the total amount.",
                    },
                ],
            }
        ],
    )

url = "https://ocr.space/Content/Images/receipt-ocr-original.jpg"


receipt = extract(url)
pprint(receipt)