from datetime import datetime

def create_initial_field_extract_prompt(promotion: str):
    return f"""
You are provided with a short paragraph of text describing a product promotion.

Extract the following fields and return a JSON object:

- product_name: string
- brand: string
- discount_percentage: integer (e.g., 20 for 20%)
- promotion_start_date: ISO 8601 date (YYYY-MM-DD)
- promotion_end_date: ISO 8601 date (YYYY-MM-DD)
- eligible_retailers: list of strings (e.g., ["Tesco", "Asda"])

INSTRUCTIONS:
- Return ONLY a valid JSON object.
- Do not include backticks, markdown, or explanations.
- Missing field values should be null (JSON null).
- If year is missing, assume {datetime.today().year}.
- If month or day are missing, return null.
- Ensure all fields match the specified types exactly.

Product promotion:
{promotion}
"""

def create_retry_field_extract_prompt(promotion: str, extracted_text: str, error_msg: str):
    return f"""
You previously attempted to extract structured data from a product promotion but the output failed validation.

Your task is to CORRECT the previous output so that it passes validation.

Extract the following fields and return a JSON object:

- product_name: string
- brand: string
- discount_percentage: integer (e.g., 20 for 20%)
- promotion_start_date: ISO 8601 date (YYYY-MM-DD)
- promotion_end_date: ISO 8601 date (YYYY-MM-DD)
- eligible_retailers: list of strings (e.g., ["Tesco", "Asda"])

INSTRUCTIONS:
- Return ONLY a valid JSON object.
- Do not include backticks, markdown, or explanations.
- Output must be valid JSON parsable by Python json.loads().
- Missing field values should be null (JSON null).
- If year is missing, assume {datetime.today().year}.
- If month or day are missing, return null.
- Ensure all fields match the specified types exactly.
- Use the error message to identify what was wrong and fix it.
- Only modify fields that are incorrect.
- Preserve correct values from the previous output.

Product promotion:
{promotion}

Previous output:
{extracted_text}

Validation error:
{error_msg}
"""