import json
import requests

from personal_notion_bot import config


class Integration:
    pass


class Database:
    @staticmethod
    def get_list_databases():
        response = requests.get(
            "https://api.notion.com/v1/databases/", headers=config.HEADERS
        )

        databases = json.loads(response.text)
        list_databases = []
        for i in databases["results"]:
            dict_i = {}
            dict_i.setdefault("id", i["id"])
            dict_i.setdefault("title", i["title"][0]["text"]["content"])
            dict_i.setdefault("properties", i["properties"])
            list_databases.append(dict_i)
        return list_databases

    def get_database(self, database_id):
        response = requests.get(
            "https://api.notion.com/v1/databases/" + f"{database_id}",
            headers=config.HEADERS,
        )

        data_database = json.loads(response.text)

        return data_database

    def get_columns_names(self, data):
        columns_names = list(data["properties"])
        return columns_names

    def get_type_column(self, data, name_column):
        type_column = data["properties"][name_column]["type"]
        return type_column


class Page:
    data_post = config.data_post

    def __init__(self, database_id):
        Page.data_post["parent"]["database_id"] = str(database_id)

    def chose_database(self, new_id):
        Page.data_post["parent"]["database_id"] = str(new_id)

    def make_title(self, title, column_name="Имя"):
        Page.data_post["properties"].setdefault(
            str(column_name), {"title": [{"text": {"content": str(title)}}]}
        )

    def make_rich_text(self, text, column_name):
        Page.data_post["properties"].setdefault(
            str(column_name), {"rich_text": [{"text": {"content": str(text)}}]}
        )

    def make_select(self, name, column_name):
        Page.data_post["properties"].setdefault(
            str(column_name), {"select": {"name": str(name)}}
        )

    def make_multi_select(self, *args, column_name):
        tags_list = Page.data_post["properties"].setdefault(
            str(column_name), {"multi_select": []}
        )
        for arg in args:
            arg_dict = {"name": str(arg)}
            tags_list["multi_select"].append(arg_dict)

    def make_date(self, start, column_name):
        Page.data_post["properties"].setdefault(
            str(column_name), {"date": {"start": str(start)}}
        )

    def make_relation(self, *args, column_name):
        arg_list = Page.data_post["properties"].setdefault(
            str(column_name), {"relation": []}
        )
        for arg in args:
            arg_dict = {"id": str(arg)}
            arg_list["relation"].append(arg_dict)

    def make_people(self, *args, column_name):
        arg_list = Page.data_post["properties"].setdefault(
            str(column_name), {"people": []}
        )
        for arg in args:
            arg_dict = {"object": "user", "id": str(arg)}
            arg_list["people"].append(arg_dict)

    def make_checkbox(self, state, column_name):
        if str(state) == "true" or state == "false":
            Page.data_post["properties"].setdefault(
                str(column_name), {"checkbox": str(state)}
            )
        else:
            return "Input isn't correct"

    def make_url(self, url, column_name):
        Page.data_post["properties"].setdefault(str(column_name), {"url": str(url)})

    def make_email(self, email, column_name):
        Page.data_post["properties"].setdefault(str(column_name), {"email": str(email)})

    def make_phone_number(self, phone_number, column_name):
        Page.data_post["properties"].setdefault(
            str(column_name), {"phone_number": str(phone_number)}
        )

    def make_number(self, number, column_name):
        Page.data_post["properties"].setdefault(
            str(column_name), {"number": float(number)}
        )

    def add_children(self, content):
        Page.data_post["children"].append(
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {"text": [{"type": "text", "text": {"content": content}}]},
            }
        )

    @staticmethod
    def post_page():
        data_json = json.dumps(Page.data_post)

        f = requests.post(
            "https://api.notion.com/v1/pages", headers=config.HEADERS, data=data_json
        )
        print(f)

    # Templates

    @staticmethod
    def make_streaming_task():
        Page.data_post["properties"] = {
            "Статус": {"select": {"name": "To Do"}},
            "Приоритет": {"select": {"name": "6 - не назначен"}},
            "Тип": {"select": {"name": "Свободная задача"}},
        }

    @staticmethod
    def make_task():
        Page.data_post["properties"] = {
            "Статус": {"select": {"name": "To Do"}},
            "Приоритет": {"select": {"name": "6 - не назначен"}},
            "Тип": {"select": {"name": "Задача"}},
        }

    @staticmethod
    def make_project():
        Page.data_post["properties"] = {
            "Статус": {"select": {"name": "To Do"}},
            "Приоритет": {"select": {"name": "6 - не назначен"}},
            "Тип": {"select": {"name": "Проект"}},
        }

    @staticmethod
    def make_epic():
        Page.data_post["properties"] = {
            "Статус": {"select": {"name": "To Do"}},
            "Приоритет": {"select": {"name": "6 - не назначен"}},
            "Тип": {"select": {"name": "Эпик"}},
        }


class Block:
    pass


class User:
    pass


def get_id(url):
    split_url = url.split("/")
    for i in split_url:
        if "?" in i:
            database_id = i.split("?")[0]
            return database_id
        else:
            return "URL isn't correct"


def get_page(page_id):
    response = requests.get(
        "https://api.notion.com/v1/pages/" + f"{page_id}", headers=config.HEADERS
    )

    data = json.loads(response.text)

    return data


def get_block(block_id):
    response = requests.get(
        "https://api.notion.com/v1/blocks/" + f"{block_id}/children?page_size=100",
        headers=config.HEADERS,
    )

    data = json.loads(response.text)

    return data


def get_tags(data, name_column):
    if Database.get_type_column(data, name_column) == "select":
        tags = data["properties"][name_column]["select"]["options"]
        return tags
    elif Database.get_type_column(data, name_column) == "multi_select":
        tags = data["properties"][name_column]["select"]["options"]
        return tags
    else:
        return "Sorry,\nThis type of column haven't got any tags."


def patch_block_children():
    pass


def search(title="", direction="ascending", timestamp="last_edited_time"):
    data = {"query": title, "direction": direction, "timestamp": timestamp}
    data_json = json.dumps(data)
    requests.post(
        "https://api.notion.com/v1/search", headers=config.HEADERS, data=data_json
    )


if __name__ == "__main__":
    page = Page("e9480f7ff4cb499d80cc47df24150517")
    page.make_streaming_task()
    page.make_title("POOOOOO")
    page.add_children("blubllulululu")
    page.post_page()
    # data = Database.get_list_databases()
    # print(data)
    # page = get_page('96708a247ad546f6bb70d8a0f83e52a2')
    # print(page)
    # page1 = Page('eb1505f59de444799a099bf99e84fd4e')
    # page1.make_title("TEST_PAGE")
    # page1.make_children("CONTENT")
    # page1.chose_database('eb1505f59de444799a099bf99e84fd4e')
    # page1.post_page()

    # {"parent": {"database_id": "eb1505f59de444799a099bf99e84fd4e"},
    # "properties": {"Name": {"title": [{"text": {"content": "Test_Name"}}]},
    # "Content": {"rich_text": [{"text": {"content": "TestTestTestTestTest"}}]}}}

    # data = get_database('eb1505f59de444799a099bf99e84fd4e')
    # print(data)
    # data_list = get_columns_names(data)
    # print(data_list)
    # for i in data_list:
    #     print(get_type_column(data, i))
