from dotenv import load_dotenv
from google import genai
from prompts import create_initial_field_extract_prompt
from schema import ProductPromotion
import json

#loads gemini api key as environment variable
load_dotenv() 

with open("inputs/sample_promotion.txt", "r",encoding="utf-8") as f:
    promotion_text = f.read()

client = genai.Client()
model = "gemini-3-flash-preview"

initial_prompt = create_initial_field_extract_prompt(promotion_text)

try:
    response = client.models.generate_content(model = model, contents=initial_prompt)
    extracted_text = response.text
    print("Raw LLM response text:", extracted_text)
    extracted_json = json.loads(extracted_text)
    product_promotion = ProductPromotion(**extracted_json)
    print("Successfully extracted data!")
    print(product_promotion)
    with open("outputs/sample_promotion_extracted.json","w") as f:
        f.write(product_promotion.model_dump_json(indent=2))
except Exception as e:
    print("Error while trying to extract data:",e)
