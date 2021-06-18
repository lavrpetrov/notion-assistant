import requests
import json
import sys; sys.path.append("..")

from config import HEADERS


def get_id(url):

    first_step = url.split("/")
    for i in first_step:
        if "?" in i:
            ID = i.split("?")[0]

    return ID


def get_database(database_id):

    response = requests.get("https://api.notion.com/v1/databases/" + f"{database_id}", headers=HEADERS)

    data = json.loads(response.text)

    return data


def get_page(page_id):

    response = requests.get("https://api.notion.com/v1/pages/" + f"{page_id}", headers=HEADERS)

    data = json.loads(response.text)

    return data


def get_block(block_id):

    response = requests.get("https://api.notion.com/v1/blocks/" + f"{block_id}/children?page_size=100", headers=HEADERS)

    data = json.loads(response.text)

    return data




def get_columns_names(data):
    keys_list = list(data['properties'])
    return keys_list


def get_type_column(data, properti):
    type_column = data['properties'][properti]['type']
    return type_column


def get_tags(data, properti):
    if get_type_column(data, properti) == "select":
        tags = data['properties'][properti]['select']['options']
        return tags
    elif get_type_column(data, properti) == "multi_select":
        tags = data['properties'][properti]['select']['options']
        return tags
    else:
        return "Sorry,\nThis type of column haven't got any tags."


def prepare_data_for_filling(data):
    for i in get_columns_names(data):
        if get_type_column(data, i) == "rich_text":
            data['properties'][i]['rich_text'].setdefault('content', '')


def prepare_data_for_posting(data, database_id):
    data_tmp1 = {'parent': {'type': 'database_id', 'database_id': ''}}
    data_tmp1['parent']['database_id'] = database_id

    data_tmp2 = {'properties': data['properties']}

    data = data_tmp1 | data_tmp2

    return data


def set_page_name(data, page_name):
    data['properties']['Name']['title'] = [{'type': 'text', 'text': {'content': page_name}}]


def path_block_children(block_id):
    pass





def post_page(data):
	data_json = json.dumps(data)

	requests.post('https://api.notion.com/v1/pages', headers=HEADERS, data=data_json)

if __name__ == '__main__':
    func_send_page("Test_Name", "TestTestTestTestTest")

