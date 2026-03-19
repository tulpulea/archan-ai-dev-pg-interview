from dotenv import load_dotenv
from google import genai
from prompts import create_initial_field_extract_prompt, create_retry_field_extract_prompt
from schema import ProductPromotion
import json

#loads gemini api key as environment variable
load_dotenv() 
input_name = "sample_promotion"
with open(f"inputs/{input_name}.txt", "r",encoding="utf-8") as f:
    promotion_text = f.read()

client = genai.Client()
model = "gemini-3-flash-preview"
initial_prompt = create_initial_field_extract_prompt(promotion_text)
error_msg = None
try:
    response = client.models.generate_content(model = model, contents=initial_prompt)
    extracted_text = response.text
    print("Raw LLM response text:", extracted_text)
    extracted_json = json.loads(extracted_text)
    product_promotion = ProductPromotion(**extracted_json)
    print("Successfully extracted data!")
    print(product_promotion)
    with open(f"outputs/{input_name}_extracted.json","w") as f:
        f.write(product_promotion.model_dump_json(indent=2))
except Exception as e:
    print("Error while trying to extract data:",e)
    error_msg = e

failures = 0
if error_msg is not None:
    for _ in range(3):
        retry_prompt = create_retry_field_extract_prompt(promotion_text, extracted_text, error_msg)
        try:
            response = client.models.generate_content(model = model, contents=retry_prompt)
            extracted_text = response.text
            print("Raw LLM response text:", extracted_text)
            extracted_json = json.loads(extracted_text)
            product_promotion = ProductPromotion(**extracted_json)
            print("Successfully extracted data!")
            print(product_promotion)
            with open(f"outputs/{input_name}_extracted.json","w") as f:
                f.write(product_promotion.model_dump_json(indent=2))
            break
        except Exception as e:
            error_msg = e
            failures += 1

if failures == 3:
    print("Data Validation Failed: Re-attempted to validate data 3 times")
