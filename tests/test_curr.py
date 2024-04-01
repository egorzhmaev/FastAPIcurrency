import pytest
from pydantic import ValidationError

from src.currency.schemas import CurrencyPair


def test_currency_pair_model():
    currency_pair_data = {'base': 'USD', 'quote': 'EUR', 'amount': 100}
    currency_pair = CurrencyPair(**currency_pair_data)
    assert currency_pair.model_dump() == currency_pair_data

    # Попытка создать CurrencyPair с недопустимыми значениями
    with pytest.raises(ValidationError):
        CurrencyPair(base='US', quote='EUR', amount=100)  # Недопустимый код валюты и отрицательное количество
    with pytest.raises(ValidationError):
        CurrencyPair(base='USD', quote='EUR', amount=-100)
    with pytest.raises(ValidationError):
        CurrencyPair(base='USD', quote='USD', amount=100)