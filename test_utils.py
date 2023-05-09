from utils import get_operations, get_executed, get_last_5, get_data_format

path_json = "operations.json"


def test_get_operations():
    operations = get_operations(path_json)
    assert isinstance(operations, list)


def test_get_executed(test_operations):
    assert get_executed(test_operations[:2]) == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }
    ]


def test_get_last_5(test_operations):
    last_5 = get_last_5(test_operations)
    assert [x['date'] for x in last_5] == ["2019-08-26T10:50:58.294041", "2019-07-03T18:35:29.512364",
                                           "2018-10-14T08:21:33.419441", "2018-07-11T02:26:18.671407",
                                           "2018-01-26T15:40:13.413061"]


def test_get_data_format(test_operations):
    data_format = get_data_format(test_operations)
    assert data_format == ['26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет  **9589\n'
                           '31957.58 руб.', '14.10.2018 Перевод с карты на счет\n'
                           'Maestro 3928 54** **** 4026 -> Счет  **3493\n77751.04 руб.',
                           '03.07.2019 Перевод организации\nMasterCard 7158 30** **** 6758 -> Счет  **5560\n'
                           '8221.37 USD', '11.07.2018 Открытие вклада\n  -> Счет  **6215\n'
                           '79931.03 руб.', '26.01.2018 Перевод с карты на счет\n'
                           'Maestro 4598 30** **** 4501 -> Счет  **5086\n50870.71 руб.']


