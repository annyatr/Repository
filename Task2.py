import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
INDENT = 4

def task() -> None:
    with open(INPUT_FILENAME) as i_f:
        csv_data = [dict_ for dict_ in csv.DictReader(i_f)]

    with open(OUTPUT_FILENAME, 'w') as o_f:
        json.dump(csv_data, o_f, indent = INDENT)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")