from dotenv import load_dotenv
from google import genai

#loads gemini api key as environment variable
load_dotenv() 

with open("inputs/sample_promotion.txt", "r",encoding="utf-8") as f:
    promotion_text = f.read()

client = genai.Client()

response = client.models.generate_content(
    model = "gemini-3-flash-preview",
    contents=f"""
Read the following product promotion text and extract:
- product name
- brand
- percentage discount
- promotion start date
- promotion end date
- list of eligible retailers

Return ONLY a valid JSON object with these fields.
Do not include any extra text.

Product promotion:
{promotion_text}
"""
)

print(response.text)

