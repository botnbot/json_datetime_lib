import pytest

from src.parsing_json import get_weekdays_sales


@pytest.fixture
def sample_sales_data():
    return {'sales': [
        {'date': '2022-10-01', 'price': 20.0, 'quantity': 100},
        {'date': '2022-10-02', 'price': 20.0, 'quantity': 120},
        {'date': '2022-10-03', 'price': 50.0, 'quantity': 40},
        {'date': '2022-10-04', 'price': 50.0, 'quantity': 60},
        {'date': '2022-10-05', 'price': 35.0, 'quantity': 70}
    ]}


# def test_get_data():
#     get_data()
#     assert


def test_get_weekdays_sales(sample_sales_data):
    weekdays_sales = get_weekdays_sales(sample_sales_data)
    assert weekdays_sales == {'2022-10-01': [{'date': '2022-10-01', 'price': 20.0, 'quantity': 100}],
                              '2022-10-02': [{'date': '2022-10-02', 'price': 20.0, 'quantity': 120}],
                              '2022-10-03': [{'date': '2022-10-03', 'price': 50.0, 'quantity': 40}],
                              '2022-10-04': [{'date': '2022-10-04', 'price': 50.0, 'quantity': 60}],
                              '2022-10-05': [{'date': '2022-10-05', 'price': 35.0, 'quantity': 70}]
                              }
