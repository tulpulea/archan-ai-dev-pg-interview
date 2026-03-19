from src.schema import ProductPromotion
from datetime import datetime
import pytest

class TestSchemaValidation:
    def test_successful_validation(self):
        test_data = {
            "product_name": "3-in-1 Pods",
            "brand": "Ariel",
            "discount_percentage": 20,
            "promotion_start_date": "2026-04-01",
            "promotion_end_date": "2026-04-30",
            "eligible_retailers": ["Tesco","Asda"]
        }
        product_promotion = ProductPromotion(**test_data)
        assert product_promotion.product_name == "3-in-1 Pods"
        assert product_promotion.brand == "Ariel"
        assert product_promotion.discount_percentage == 20
        assert product_promotion.promotion_start_date == datetime.strptime("2026-04-01","%Y-%m-%d").date()
        assert product_promotion.promotion_end_date == datetime.strptime("2026-04-30","%Y-%m-%d").date()
        assert product_promotion.eligible_retailers == ["Tesco","Asda"]

    def test_empty_null_vals(self):
        test_data = {
            "product_name": "3-in-1 Pods",
            "brand": "",
            "discount_percentage": None,
            "promotion_start_date": "2026-04-01",
            "promotion_end_date": "2026-04-30",
            "eligible_retailers": []
        }
        product_promotion = ProductPromotion(**test_data)
        assert product_promotion.product_name == "3-in-1 Pods"
        assert product_promotion.brand == ""
        assert product_promotion.discount_percentage is None
        assert product_promotion.promotion_start_date == datetime.strptime("2026-04-01","%Y-%m-%d").date()
        assert product_promotion.promotion_end_date == datetime.strptime("2026-04-30","%Y-%m-%d").date()
        assert product_promotion.eligible_retailers == []

    def test_invalid_date(self):
        test_data = {
            "product_name": "3-in-1 Pods",
            "brand": "Ariel",
            "discount_percentage": 20,
            "promotion_start_date": "04/01/2026",
            "promotion_end_date": None,
            "eligible_retailers": ["Tesco","Asda"]
        }
        with pytest.raises(ValueError):
            product_promotion = ProductPromotion(**test_data)

    def test_invalid_retailers(self):
        test_data = {
            "product_name": "3-in-1 Pods",
            "brand": "Ariel",
            "discount_percentage": 20,
            "promotion_start_date": "2026-04-01",
            "promotion_end_date": "2026-04-30",
            "eligible_retailers": "Tesco"
        }
        with pytest.raises(ValueError):
            product_promotion = ProductPromotion(**test_data)
