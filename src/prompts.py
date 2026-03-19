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