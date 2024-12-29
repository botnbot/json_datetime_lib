from collections import Counter

from src.parsing_json import get_data, get_totals_by_weekdays, get_weekdays_sales


def main():
    data = get_data("data/data.json")
    sales_by_weekdays = get_weekdays_sales(data)
    totals_by_weekdays = get_totals_by_weekdays(sales_by_weekdays)
    best_days = Counter(totals_by_weekdays).most_common()
    print(f"Рейтинг по дням недели: {best_days[0:]}")
    return


if __name__ == '__main__':
    main()
