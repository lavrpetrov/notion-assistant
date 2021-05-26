import requests
import json
from pathlib import Path

from config.py import NOTION_TOKEN, DATABASE_ID

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



def sendPage(Page_Name, Page_Content):
    '''Функция пушит пейдж в конкретную базу данных в Notion.

    Эта функция принимает 2 аргумента: название странички и её содержимое.
    '''
    data["properties"]["Name"]["title"][0]["text"]["content"] = str(Page_Name)
    data["properties"]["Content"]["rich_text"][0]["text"]["content"] = str(Page_Content)
    
    data_json = json.dumps(data)

    requests.post('https://api.notion.com/v1/pages', headers=HEADERS, data=data_json)


sendPage(126, "TestTestTestTestTest")



#def sendPage(Page_Name, Page_Content): 
#    data = '{"parent": { "database_id": "a0bcd55c56194c37be040cc35bda0d1e" }, "properties": {"Name": {"title": [{"text": {"content": f"{Page_Name}"}}]}, "Content": {"rich_text": [{"text": {"content": f"{Page_Content}"}}]}}}'





