from collections import Counter
from pprint import pprint

from src.parsing_json import get_data, get_weekdays_sales, get_totals_by_weekdays

data = get_data("data/data.json")
sales_by_weekdays = get_weekdays_sales(data)
totals_by_weekdays = get_totals_by_weekdays(sales_by_weekdays)
best_days = Counter(totals_by_weekdays).most_common()
# print(f'Лучший день для продаж {best_days[0][0]} сумма {best_days[0][1]}')
# print(f'{best_days[1][0]} тоже не плох с суммой {best_days[1][1]}')
pprint(f"Рейтинг по дням недели: {best_days[0:]}")
