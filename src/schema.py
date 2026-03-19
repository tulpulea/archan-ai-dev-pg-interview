from datetime import date, datetime
from pydantic import BaseModel, PositiveInt, ValidationError, field_validator

class ProductPromotion(BaseModel):
    product_name: str | None
    brand: str | None
    discount_percentage: PositiveInt | None
    promotion_start_date: date | None
    promotion_end_date : date | None
    eligible_retailers: list[str] | None

    @field_validator("promotion_start_date", "promotion_end_date", mode="before")
    @classmethod
    def validate_date(cls, value: str):
        if value is None:
            return value
        try:
            formatted_date = datetime.strptime(value, "%Y-%m-%d")
            return formatted_date.date()
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format")
        






