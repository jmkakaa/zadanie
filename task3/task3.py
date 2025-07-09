import json
import sys


def read_json(values: str):
    with open(values, "r", encoding="utf-8") as f:
        data = json.load(f)
        return {str(item['id']): item['value'] for item in data['values']}

def update(data, value_map):
    if isinstance(data, dict):
        if 'id' in data and 'value' in data and data['value'] == "":
            id_str = str(data['id'])
            if id_str in value_map:
                data['value'] = value_map[id_str]
        for i in data:
            update(data[i], value_map)
    elif isinstance(data, list):
        for i in data:
            update(i, value_map)

def write_report(tests: str, reports: str, value_map):
    with open(tests, "r", encoding="utf-8") as f:
        data = json.load(f)
        update(data, value_map)

    with open(reports, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    tests, values, report = sys.argv[1:4]
    value_map = read_json(values)
    write_report(tests, report, value_map)


