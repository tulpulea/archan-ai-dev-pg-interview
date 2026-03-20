from src.extractor import run_extraction
from textwrap import dedent
from datetime import datetime
import pytest

class TestPipeline:
    def test_initial_fake_llm_success(self):
        test_promo = "test"
        def fake_llm(prompt):
            return dedent("""
                    {
                    "product_name": "3-in-1 Pods",
                    "brand": "Ariel",
                    "discount_percentage": 20,
                    "promotion_start_date": "2026-04-01",
                    "promotion_end_date": "2026-04-30",
                    "eligible_retailers": ["Tesco", "Asda"]
                    }
                    """)
        product_info = run_extraction(test_promo, fake_llm)
        assert product_info.product_name == "3-in-1 Pods"
        assert product_info.brand == "Ariel"
        assert product_info.discount_percentage == 20
        assert product_info.promotion_start_date == datetime.strptime("2026-04-01","%Y-%m-%d").date()
        assert product_info.promotion_end_date == datetime.strptime("2026-04-30","%Y-%m-%d").date()
        assert product_info.eligible_retailers == ["Tesco","Asda"]
    
    def test_fake_llm_first_retry_success(self):
        test_promo = "test"
        calls = []
        def fake_llm(prompt):
            if len(calls) < 1:
                calls.append(1)
                #bad json - missing closing curly bracket }
                return dedent("""
                        {
                        "product_name": "3-in-1 Pods",
                        "brand": "Ariel",
                        "discount_percentage": 20,
                        "promotion_start_date": "2026-04-01",
                        "promotion_end_date": "2026-04-30",
                        "eligible_retailers": ["Tesco", "Asda"]
                        """)                
            return dedent("""
                    {
                    "product_name": "3-in-1 Pods",
                    "brand": "Ariel",
                    "discount_percentage": 20,
                    "promotion_start_date": "2026-04-01",
                    "promotion_end_date": "2026-04-30",
                    "eligible_retailers": ["Tesco", "Asda"]
                    }
                    """)
        product_info = run_extraction(test_promo, fake_llm)
        assert product_info.product_name == "3-in-1 Pods"
        assert product_info.brand == "Ariel"
        assert product_info.discount_percentage == 20
        assert product_info.promotion_start_date == datetime.strptime("2026-04-01","%Y-%m-%d").date()
        assert product_info.promotion_end_date == datetime.strptime("2026-04-30","%Y-%m-%d").date()
        assert product_info.eligible_retailers == ["Tesco","Asda"]

    def test_fake_llm_second_retry_success(self):
        test_promo = "test"
        calls = []
        def fake_llm(prompt):
            if len(calls) < 2:
                calls.append(1)
                #bad json - missing closing curly bracket }
                return dedent("""
                        {
                        "product_name": "3-in-1 Pods",
                        "brand": "Ariel",
                        "discount_percentage": 20,
                        "promotion_start_date": "2026-04-01",
                        "promotion_end_date": "2026-04-30",
                        "eligible_retailers": ["Tesco", "Asda"]
                        """)                
            return dedent("""
                    {
                    "product_name": "3-in-1 Pods",
                    "brand": "Ariel",
                    "discount_percentage": 20,
                    "promotion_start_date": "2026-04-01",
                    "promotion_end_date": "2026-04-30",
                    "eligible_retailers": ["Tesco", "Asda"]
                    }
                    """)
        product_info = run_extraction(test_promo, fake_llm)
        assert product_info.product_name == "3-in-1 Pods"
        assert product_info.brand == "Ariel"
        assert product_info.discount_percentage == 20
        assert product_info.promotion_start_date == datetime.strptime("2026-04-01","%Y-%m-%d").date()
        assert product_info.promotion_end_date == datetime.strptime("2026-04-30","%Y-%m-%d").date()
        assert product_info.eligible_retailers == ["Tesco","Asda"]

    def test_fake_llm_third_retry_success(self):
        test_promo = "test"
        calls = []
        def fake_llm(prompt):
            if len(calls) < 2:
                calls.append(1)
                #bas json - missing closing curly bracket }
                return dedent("""
                        {
                        "product_name": "3-in-1 Pods",
                        "brand": "Ariel",
                        "discount_percentage": 20,
                        "promotion_start_date": "2026-04-01",
                        "promotion_end_date": "2026-04-30",
                        "eligible_retailers": ["Tesco", "Asda"]
                        """)     
            if len(calls) < 3:
                calls.append(1)
                #fail validation - wrong date format   
                return dedent("""
                        {
                        "product_name": "3-in-1 Pods",
                        "brand": "Ariel",
                        "discount_percentage": 20,
                        "promotion_start_date": "04/01/2026",
                        "promotion_end_date": "2026-04-30",
                        "eligible_retailers": ["Tesco", "Asda"]
                        """)       
            return dedent("""
                    {
                    "product_name": "3-in-1 Pods",
                    "brand": "Ariel",
                    "discount_percentage": 20,
                    "promotion_start_date": "2026-04-01",
                    "promotion_end_date": "2026-04-30",
                    "eligible_retailers": ["Tesco", "Asda"]
                    }
                    """)
        product_info = run_extraction(test_promo, fake_llm)
        assert product_info.product_name == "3-in-1 Pods"
        assert product_info.brand == "Ariel"
        assert product_info.discount_percentage == 20
        assert product_info.promotion_start_date == datetime.strptime("2026-04-01","%Y-%m-%d").date()
        assert product_info.promotion_end_date == datetime.strptime("2026-04-30","%Y-%m-%d").date()
        assert product_info.eligible_retailers == ["Tesco","Asda"]

    def test_fake_llm_three_failed_retries_failure(self):
        test_promo = "test"
        calls = []
        def fake_llm(prompt):
            if len(calls) < 4:
                calls.append(1)
                #bas json - missing closing curly bracket }
                return dedent("""
                        {
                        "product_name": "3-in-1 Pods",
                        "brand": "Ariel",
                        "discount_percentage": 20,
                        "promotion_start_date": "2026-04-01",
                        "promotion_end_date": "2026-04-30",
                        "eligible_retailers": ["Tesco", "Asda"]
                        """)                
            return dedent("""
                    {
                    "product_name": "3-in-1 Pods",
                    "brand": "Ariel",
                    "discount_percentage": 20,
                    "promotion_start_date": "2026-04-01",
                    "promotion_end_date": "2026-04-30",
                    "eligible_retailers": ["Tesco", "Asda"]
                    }
                    """)
        with pytest.raises(RuntimeError):
            product_info = run_extraction(test_promo, fake_llm)