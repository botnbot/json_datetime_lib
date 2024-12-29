from datetime import datetime
from json import load


def get_data(path: str) -> list[dict]:
    """Функция получает на вход путь к JSON-файлу и возвращает список словарей с продажами"""
    with open(path, "r") as datafile:
        return load(datafile)


def get_weekdays_sales(data: list[dict]) -> dict:
    """Функция принимает список словарей с продажами и возвращает словарь, где ключи - это даты, а значения - данные
    о продажах в этот день"""
    total = {}
    for sale in data["sales"]:
        date = sale.get("date")
        if not date:
            print(f"нет данных {sale}")
            continue
        if date not in total:
            total[date] = []
        total[date].append(sale)
    return total


def get_totals_by_weekdays(sales: dict) -> dict:
    """Функция принимает на вход словарь, где ключи - это даты, а значения - данные
    о продажах в этот день и возвращает словарь с суммами продаж по дням недели"""
    result = {}
    for date, sales in sales.items():
        daily_total = sum(sale["price"] * sale["quantity"] for sale in sales)
        day = datetime.strptime(date, "%Y-%m-%d").strftime("%A")
        if day not in result:
            result[day] = 0
        result[day] += daily_total
    return result
