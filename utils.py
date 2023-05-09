import json
from operator import itemgetter
from datetime import datetime


def get_operations(path):
    with open(path, 'r', encoding='utf-8') as file:
        operations = json.load(file)
    return operations


def get_executed(operations):
    executed_operations = []
    for operation in operations:
        if "state" in operation and operation["state"] == "EXECUTED":
            executed_operations.append(operation)

    return executed_operations


def get_last_5(executed_operations):
    last_5 = sorted(executed_operations, key=itemgetter('date'), reverse=True)
    return last_5[:5]


def get_data_format(last_5):
    data_format = []
    for item in last_5:
        date = datetime.strptime(item['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = item['description']

        if 'from' in item:
            split_from = item['from'].split()
            bill_from = split_from.pop(-1)
            info_from = " ".join(split_from)
            account_from = f"{bill_from[:4]} {bill_from[4:6]}**" \
                           f" **** {bill_from[-4:]}"
        else:
            info_from, account_from = "", ""

        info_to = item['to'].split()[0]
        account_to = f" **{item['to'][-4:]}"
        amount = f"{item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}"

        data_format.append(f"""\
{date} {description}
{info_from} {account_from} -> {info_to} {account_to}
{amount}""")
    return data_format
