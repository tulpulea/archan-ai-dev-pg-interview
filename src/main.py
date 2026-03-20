def main(input_name: str):
    from dotenv import load_dotenv
    from google import genai
    from io_utils import read_txt_input, write_json_output
    from llm import create_llm_wrapper
    from extractor import run_extraction

    #loads gemini api key as environment variable
    load_dotenv() 
    promotion_text = read_txt_input(input_name)
    client = genai.Client()
    model = "gemini-3-flash-preview"
    llm_wrapper = create_llm_wrapper(client, model)
    try:
        product_info_extracted = run_extraction(promotion_text,llm_wrapper)
        write_json_output(product_info_extracted, input_name)
        print(f"Product data extracted successfully and output saved to {input_name}_extracted.json")
    except RuntimeError as e:
        print("Product data extraction failed.")
        print(e)

if __name__ == "__main__":
    main("sample_promotion")

