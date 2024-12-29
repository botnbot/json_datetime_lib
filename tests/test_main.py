from unittest.mock import patch


@patch(
    "src.parsing_json.get_data",
    return_value={
        "sales": [
            {"date": "2022-10-02", "price": 20.0, "quantity": 120},
            {"date": "2022-10-04", "price": 50.0, "quantity": 60},
            {"date": "2022-10-05", "price": 35.0, "quantity": 70},
        ]
    },
)
def test_main(mock_get_data, capsys):
    from main import main

    main()
    captured = capsys.readouterr()
    expected_output = "Рейтинг по дням недели: [('Tuesday', 3000.0), ('Wednesday', 2450.0), ('Sunday', 2400.0)]"
    assert expected_output in captured.out
