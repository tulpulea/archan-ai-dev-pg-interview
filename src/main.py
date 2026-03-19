from dotenv import load_dotenv

#loads gemini api key as environment variable
load_dotenv() 

with open("inputs/sample_promotion.txt", "r",encoding="utf-8") as f:
    promotion_text = f.read()

print(promotion_text)
