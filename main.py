from utils import get_operations, get_executed, get_last_5, get_data_format

PATH_JSON = "operations.json"


def main():
    operations = get_operations(PATH_JSON)
    executed_operations = get_executed(operations)
    last_5_executed = get_last_5(executed_operations)
    data_format = get_data_format(last_5_executed)

    for item in data_format:
        print(item, end='\n\n')


if __name__ == '__main__':
    main()
