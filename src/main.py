from dotenv import load_dotenv
from google import genai
from prompts import create_initial_field_extract_prompt

#loads gemini api key as environment variable
load_dotenv() 

with open("inputs/sample_promotion.txt", "r",encoding="utf-8") as f:
    promotion_text = f.read()

client = genai.Client()
model = "gemini-3-flash-preview"

initial_prompt = create_initial_field_extract_prompt(promotion_text)

print(initial_prompt)
