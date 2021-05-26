import requests
import json
from pathlib import Path


NOTION_TOKEN = Path('/home/roman/Programming/GitHub/personal-notion-bot/config/notion.token').read_text().strip()

HEADERS = {
    'Authorization': 'Bearer secret_bU5kuB9GvU6sMVi3V0tRhLGntKQuxwXUr0LWiBKsX8b',
    'Content-Type': 'application/json',
    'Notion-Version': '2021-05-13',
}

data = {}

data.setdefault("parent", {})
data["parent"].setdefault("database_id", "a0bcd55c56194c37be040cc35bda0d1e")
data.setdefault("properties", {})
data["properties"].setdefault("Name", {})
data["properties"].setdefault("Content", {})
data["properties"]["Name"].setdefault("title", [{"text": {"content": ''}}])
data["properties"]["Content"].setdefault("rich_text", [{"text": {"content": ''}}])



def sendPage(Page_Name, Page_Content):
    data["properties"]["Name"]["title"][0]["text"]["content"] = str(Page_Name)
    data["properties"]["Content"]["rich_text"][0]["text"]["content"] = str(Page_Content)
    
    data_json = json.dumps(data)

    requests.post('https://api.notion.com/v1/pages', headers=HEADERS, data=data_json)


sendPage(126, "TestTestTestTestTest")



#def sendPage(Page_Name, Page_Content): 
#    data = '{"parent": { "database_id": "a0bcd55c56194c37be040cc35bda0d1e" }, "properties": {"Name": {"title": [{"text": {"content": f"{Page_Name}"}}]}, "Content": {"rich_text": [{"text": {"content": f"{Page_Content}"}}]}}}'





