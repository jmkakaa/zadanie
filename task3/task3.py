import json
from imghdr import tests


def read_values(values: str):
    with open(values, "r", encoding="utf-8") as fread:
        data = json.load(fread)
        return {str(item['id']): item['value'] for item in data['values']}


def write_report(tests: str, report: str):
    value_map = read_values()
    result_lines = []

    with open(tests, "r", encoding="utf-8") as fread:
        for line in fread:
            stripped = line.strip()

            if stripped.startswith('"id":'):
                current_id = stripped.split(":")[1].strip().rstrip(",")
                current_id = current_id.replace(" ", "").replace(",", "").replace('"', '')

            if stripped.startswith('"value": ""'):
                if current_id in value_map:
                    value = value_map[current_id]
                    line = f'      "value": "{value}"\n'

            result_lines.append(line)

    with open(report, "w", encoding="utf-8") as fwrite:
        fwrite.writelines(result_lines)


if __name__ == '__main__':
    tests = "tests.json"
    values = "values.json"
    report = "report.json"
    read_values(values)
    write_report(tests, report)
