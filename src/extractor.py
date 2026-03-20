import json
from schema import ProductPromotion
from prompts import create_initial_field_extract_prompt, create_retry_field_extract_prompt

def run_extraction(promo_text: str, llm_extraction_func: function):
    initial_prompt = create_initial_field_extract_prompt(promo_text)
    extracted_text = llm_extraction_func(initial_prompt)
    error_msg = None
    try:
        extracted_json = json.loads(extracted_text)
        product_promotion = ProductPromotion(**extracted_json)
        return product_promotion
    except Exception as e:
        error_msg = e
    
    for _ in range(3):
        retry_prompt = create_retry_field_extract_prompt(promo_text, extracted_text, error_msg)
        extracted_text = llm_extraction_func(retry_prompt)
        try:
            extracted_json = json.loads(extracted_text)
            product_promotion = ProductPromotion(**extracted_json)
            return product_promotion
        except Exception as e:
            error_msg = e
    raise RuntimeError("Data Validation Failed: Re-attempted to validate data 3 times")