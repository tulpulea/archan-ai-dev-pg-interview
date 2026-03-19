from src.prompts import create_initial_field_extract_prompt, create_retry_field_extract_prompt
from datetime import datetime

class TestInitialPromptCreation:
    def test_initial_prompt_creation(self):
        test_text = "test"
        prompt = create_initial_field_extract_prompt(test_text)
        assert "Return ONLY a valid JSON object" in prompt
        assert "Missing field values should be null (JSON null)." in prompt
        assert "promotion_start_date: ISO 8601 date (YYYY-MM-DD)" in prompt

    def test_initial_prompt_input_text(self):
        test_text = "Lord of the Rings"
        prompt = create_initial_field_extract_prompt(test_text)
        assert "Lord of the Rings" in prompt

    def test_initial_prompt_current_year(self):
        test_text = "test"
        prompt = create_initial_field_extract_prompt(test_text)
        assert str(datetime.today().year) in prompt

class TestRetryPromptCreation:
    def test_retry_prompt_creation(self):
        test_text = "test"
        prompt = create_retry_field_extract_prompt(test_text,test_text, test_text)
        assert "Return ONLY a valid JSON object" in prompt
        assert "Missing field values should be null (JSON null)." in prompt
        assert "promotion_start_date: ISO 8601 date (YYYY-MM-DD)" in prompt
        assert "Preserve correct values from the previous output." in prompt

    def test_retry_prompt_input_text(self):
        test_text = "Lord of the Rings"
        prompt = create_retry_field_extract_prompt(test_text,"","")
        assert "Lord of the Rings" in prompt

    def test_retry_prompt_current_year(self):
        test_text = "test"
        prompt = create_retry_field_extract_prompt(test_text,"","")
        assert str(datetime.today().year) in prompt

    def test_retry_prompt_prev_llm_res(self):
        test_previous_LLM_res = "Peter Pan"
        prompt = create_retry_field_extract_prompt("",test_previous_LLM_res,"")
        assert "Peter Pan" in prompt

    def test_retry_prompt_error_msg(self):
        test_error_msg = "The One Piece is real!"
        prompt = create_retry_field_extract_prompt("","",test_error_msg)
        assert "The One Piece is real!" in prompt


