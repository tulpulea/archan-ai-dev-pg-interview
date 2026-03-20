def read_txt_input(input_name: str):
    with open(f"inputs/{input_name}.txt", "r",encoding="utf-8") as f:
        promotion_text = f.read()
    return promotion_text

def write_json_output(product_promotion, input_name: str):
    with open(f"outputs/{input_name}_extracted.json","w") as f:
            f.write(product_promotion.model_dump_json(indent=2))