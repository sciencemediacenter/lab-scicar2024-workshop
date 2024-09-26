import instructor
from pydantic import BaseModel
from openai import OpenAI
import os

# Cf. https://python.useinstructor.com/#using-openai


# Define your desired output structure
class UserInfo(BaseModel):
    name: str
    age: int


# Patch the OpenAI client
client = instructor.from_openai(OpenAI(api_key=os.getenv("OPENAI_API_KEY")))

# Extract structured data from natural language
user_info = client.chat.completions.create(
    model="gpt-3.5-turbo",
    response_model=UserInfo,
    messages=[{"role": "user", "content": "John Doe is 30 years old."}],
)

print(user_info.name, type(user_info.name))
#> John Doe
print(user_info.age, type(user_info.age))
#> 30