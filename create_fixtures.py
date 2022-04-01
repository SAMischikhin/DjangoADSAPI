import csv
import json
import os
from typing import List, Union

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'datasets')
FIXTURE_DIR = os.path.join(BASE_DIR, 'fixtures')


def str_to_val(item:str) -> Union[str, bool, float, int]:
    if item == 'TRUE':
        return True
    elif item == 'FALSE':
        return False
    elif item.isdigit():
        return int(item)
    elif sum([b.isdigit() for b in item.split('.')]) == 2:
        return float(item)
    else:
        return  item


def get_cvs_dict(cvs_data_path: str) -> List[str]:
    with open(cvs_data_path, 'r', encoding='UTF-8') as csvfile:
        field_names = csvfile.readline().strip().split(',')
        return [r for r in csv.DictReader(csvfile, field_names)]


def get_row_py_dict(cvslist: List[str], name: str) -> List[str]:
    res = []
    for key, item in enumerate(cvslist):
        res.append({
            "pk": key,
            "model": f"ads.{name}",
            "fields": item
                })
    return res


def correct_py_list(py_list: List[str]) -> List[str]:
    for dic in py_list:
        dic['fields'] = dict([(key, str_to_val(dic['fields'][key])) for key in dic['fields']])
    return py_list


def get_py_dict(cvslist: List[str], name: str) -> List[str]:
    res = get_row_py_dict(cvslist, name)
    return correct_py_list(res)


def create_fixtures(data_dir: str, fixture_dir: str, file_name: str):
    cvs_data_path = os.path.join(data_dir, file_name)
    cvs_dict = get_cvs_dict(cvs_data_path)
    data = get_py_dict(cvs_dict, file_name.split('.')[0])
    json_data_path = os.path.join(fixture_dir, f'{file_name.split(".")[0]}.json')

    with open(json_data_path, 'w', encoding='UTF-8') as jsonfile:
        json.dump(data, jsonfile, sort_keys=False, indent=4, separators=(',', ': '), ensure_ascii=False)

    jsonfile.close()


for name in os.listdir(DATA_DIR):
    create_fixtures(DATA_DIR, FIXTURE_DIR, name)
