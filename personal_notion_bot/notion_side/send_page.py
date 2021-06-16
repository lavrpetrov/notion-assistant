import requests
import json
import sys; sys.path.append("..")

from config import HEADERS, DATABASE_ID


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


def get_columns_names(data):
    keys_list = list(data['properties'])
    return keys_list


def get_type_column(data, properti):
    type_column = data['properties'][properti]['type']
    return type_column


def get_tags(data, properti):
    if get_type_column(data, properti) == "select":
        pass
    elif get_type_column(data, properti) == "multi_select":
        pass
    else:
        return "Sorry,\nThis type of column haven't got any tags."


def prepare_data_for_filling(data):
    for i in get_columns_names(data):
        if get_type_column(data, i) == "rich_text":
            data['properties'][i]['rich_text'].setdefault('content', '')
        elif get_type_column(data, i) == "title":
            data['properties'][i]['title'].setdefault('content', '')
        elif get_type_column(data, i) == "multi_select":
            data['properties'][i]['multi_select'].setdefault('options', [])



data = {}

data.setdefault("parent", {})
data["parent"].setdefault("database_id", str(DATABASE_ID))
data.setdefault("properties", {})
data["properties"].setdefault("Name", {})
data["properties"].setdefault("Content", {})
data["properties"]["Name"].setdefault("title", [{"text": {"content": ''}}])
data["properties"]["Content"].setdefault("rich_text", [{"text": {"content": ''}}])


#def func_send_page(page_name, page_content):
#	'''Функция пушит пейдж в конкретную базу данных в Notion.
#
#	Эта функция принимает 2 аргумента: название странички и её содержимое.
#	'''
#	data["properties"]["Name"]["title"][0]["text"]["content"] = str(page_name)
#	data["properties"]["Content"]["rich_text"][0]["text"]["content"] = str(page_content)
#
#	data_json = json.dumps(data)
#
#	requests.post('https://api.notion.com/v1/pages', headers=HEADERS, data=data_json)
#
if __name__ == '__main__':
	func_send_page("Test_Name", "TestTestTestTestTest")

