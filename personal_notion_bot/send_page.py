import requests
import json
from pathlib import Path

from config import NOTION_TOKEN, DATABASE_ID

HEADERS = {
    'Authorization': f'Bearer {NOTION_TOKEN}',
    'Content-Type': 'application/json',
    'Notion-Version': '2021-05-13',
}

data = {}

data.setdefault("parent", {})
data["parent"].setdefault("database_id", str(DATABASE_ID))
data.setdefault("properties", {})
data["properties"].setdefault("Name", {})
data["properties"].setdefault("Content", {})
data["properties"]["Name"].setdefault("title", [{"text": {"content": ''}}])
data["properties"]["Content"].setdefault("rich_text", [{"text": {"content": ''}}])



def func_send_page(page_name, page_content):
    '''Функция пушит пейдж в конкретную базу данных в Notion.

    Эта функция принимает 2 аргумента: название странички и её содержимое.
    '''
    data["properties"]["Name"]["title"][0]["text"]["content"] = str(page_name)
    data["properties"]["Content"]["rich_text"][0]["text"]["content"] = str(page_content)
    
    data_json = json.dumps(data)

    requests.post('https://api.notion.com/v1/pages', headers=HEADERS, data=data_json)

if __name__ == '__main__':
    send_page("Test_Name", "TestTestTestTestTest")

