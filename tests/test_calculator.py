from src.calculator import add_numbers, normalize_name


def test_add_numbers() -> None:
    assert add_numbers(2, 3) == 5


def test_normalize_name() -> None:
    assert normalize_name("  databricks  ") == "Databricks"
