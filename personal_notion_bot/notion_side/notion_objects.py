import json
import requests
import config


class Integration:

    @staticmethod
    def get_list_of_databases():
        response = requests.get(
            "https://api.notion.com/v1/databases/", headers=config.HEADERS
        )

        databases = json.loads(response.text)
        list_of_databases = []
        for i in databases["results"]:
            dict_i = {}
            dict_i.setdefault("id", i["id"])
            dict_i.setdefault("title", i["title"][0]["text"]["content"])
            dict_i.setdefault("properties", i["properties"])
            list_of_databases.append(dict_i)

        return list_of_databases

    @staticmethod
    def get_list_of_users():
        response = requests.get("https://api.notion.com/v1/users", headers=config.HEADERS)

        return response

    @staticmethod
    def search(title="", value="page", direction="ascending", timestamp="created_time", page_size=1):
        '''value can be "page" or "database"'''

        data = {"query": title, "value": value, "direction": direction, "timestamp": timestamp, "page_size": page_size}
        data_json = json.dumps(data)

        response = requests.post("https://api.notion.com/v1/search", headers=config.HEADERS, data=data_json)

        data = json.loads(response.text)

        return data


class Database:

    @staticmethod
    def get_database(database_id):
        response = requests.get(
            "https://api.notion.com/v1/databases/" + f"{database_id}",
            headers=config.HEADERS,
        )

        data_database = json.loads(response.text)

        return data_database

    @staticmethod
    def get_columns_names(data):
        columns_names = list(data["properties"])
        return columns_names

    @staticmethod
    def get_type_column(data, name_column):
        type_column = data["properties"][name_column]["type"]
        return type_column


class Page:

    data_post = config.data_post

    def __init__(self, database_id):
        Page.data_post["parent"]["database_id"] = str(database_id)

    @staticmethod
    def chose_database(new_id):
        Page.data_post["parent"]["database_id"] = str(new_id)

    # Editing fields

    @staticmethod
    def make_title(title, column_name="Имя"):
        Page.data_post["properties"].setdefault(
            str(column_name), {"title": [{"text": {"content": str(title)}}]}
        )

    @staticmethod
    def make_rich_text(text, column_name):
        Page.data_post["properties"].setdefault(
            str(column_name), {"rich_text": [{"text": {"content": str(text)}}]}
        )

    @staticmethod
    def make_select(name: str, column_name: str):
        # Page.data_post["properties"].setdefault(
        #     str(column_name), {"select": {"name": str(name)}}
        # )
        Page.data_post["properties"].update({column_name: {"select": {"name": name}}})

    @staticmethod
    def make_multi_select(*args, column_name):
        tags_list = Page.data_post["properties"].setdefault(
            str(column_name), {"multi_select": []}
        )
        for arg in args:
            arg_dict = {"name": str(arg)}
            tags_list["multi_select"].append(arg_dict)

    @staticmethod
    def make_date(start, column_name):
        Page.data_post["properties"].setdefault(
            str(column_name), {"date": {"start": str(start)}}
        )

    @staticmethod
    def make_relation(*args, column_name):
        arg_list = Page.data_post["properties"].setdefault(
            str(column_name), {"relation": []}
        )
        for arg in args:
            arg_dict = {"id": str(arg)}
            arg_list["relation"].append(arg_dict)

    @staticmethod
    def make_people(*args, column_name):
        arg_list = Page.data_post["properties"].setdefault(
            str(column_name), {"people": []}
        )
        for arg in args:
            arg_dict = {"object": "user", "id": str(arg)}
            arg_list["people"].append(arg_dict)

    @staticmethod
    def make_checkbox(state, column_name):
        if str(state) == "true" or state == "false":
            Page.data_post["properties"].setdefault(
                str(column_name), {"checkbox": str(state)}
            )
        else:
            return "Input isn't correct"

    @staticmethod
    def make_url(url, column_name):
        Page.data_post["properties"].setdefault(str(column_name), {"url": str(url)})

    @staticmethod
    def make_email(email, column_name):
        Page.data_post["properties"].setdefault(str(column_name), {"email": str(email)})

    @staticmethod
    def make_phone_number(phone_number, column_name):
        Page.data_post["properties"].setdefault(
            str(column_name), {"phone_number": str(phone_number)}
        )

    @staticmethod
    def make_number(number, column_name):
        Page.data_post["properties"].setdefault(
            str(column_name), {"number": float(number)}
        )

    @staticmethod
    def add_children(content):
        Page.data_post["children"][0]["paragraph"]["text"][0]["text"]["content"] = str(content)

    # Post page to database

    @staticmethod
    def post_page():
        data_json = json.dumps(Page.data_post)

        f = requests.post(
            "https://api.notion.com/v1/pages", headers=config.HEADERS, data=data_json
        )
        print(f)

    # Templates

    @staticmethod
    def make_streaming_task(status="Сделать", priority="6 - не назначен"):
        Page.data_post["parent"]["database_id"] = "e9480f7ff4cb499d80cc47df24150517"

        Page.data_post["properties"] = {
            "Статус": {"select": {"name": status}},
            "Приоритет": {"select": {"name": priority}},
            "Тип": {"select": {"name": "Независимая задача"}},
        }

    @staticmethod
    def make_task(status="Сделать", priority="6 - не назначен"):
        Page.data_post["parent"]["database_id"] = "e9480f7ff4cb499d80cc47df24150517"

        Page.data_post["properties"] = {
            "Статус": {"select": {"name": status}},
            "Приоритет": {"select": {"name": priority}},
            "Тип": {"select": {"name": "Задача"}},
        }

    @staticmethod
    def make_project(status="Сделать", priority="6 - не назначен"):
        Page.data_post["parent"]["database_id"] = "e9480f7ff4cb499d80cc47df24150517"

        Page.data_post["properties"] = {
            "Статус": {"select": {"name": status}},
            "Приоритет": {"select": {"name": priority}},
            "Тип": {"select": {"name": "Проект"}},
        }

    @staticmethod
    def make_epic(status="Сделать", priority="6 - не назначен"):
        Page.data_post["parent"]["database_id"] = "e9480f7ff4cb499d80cc47df24150517"

        Page.data_post["properties"] = {
            "Статус": {"select": {"name": status}},
            "Приоритет": {"select": {"name": priority}},
            "Тип": {"select": {"name": "Эпик"}},
        }

    @staticmethod
    def make_purchase(urgent="Limited - Хотелки", priority="6 - не назначен"):
        Page.data_post["parent"]["database_id"] = "e9480f7ff4cb499d80cc47df24150517"

        Page.data_post["properties"] = {
            "Статус": {"select": {"name": "Сделать"}},
            "Срочность": {"select": {"name": urgent}},
            "Приоритет": {"select": {"name": priority}},
            "Тип": {"select": {"name": "Покупка"}},
        }

    # Searching page

    @staticmethod
    def get_page_id_by_title(title: str):
        page = Integration.search(title)
        invalid_page_id = page["results"][0]["id"]
        valid_page_id = "".join([l for l in invalid_page_id if l != "-"])

        return valid_page_id


    @staticmethod
    def get_page_url_by_title(title: str):
        page = Integration.search(title)
        page_url = page["results"][0]["url"]

        return page_url





class User:

    @staticmethod
    def get_user(user_id):
        response = requests.get("https://api.notion.com/v1/users/" + f"{user_id}", headers=config.HEADERS)

        data = json.loads(response.text)

        return data


class Block:
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
    if Database.get_type_column(name_column) == "select":
        tags = data["properties"][name_column]["select"]["options"]
        return tags
    elif Database.get_type_column(name_column) == "multi_select":
        tags = data["properties"][name_column]["select"]["options"]
        return tags
    else:
        return "Sorry,\nThis type of column haven't got any tags."


def patch_block_children():
    pass





if __name__ == "__main__":
    # page = Integration.search("Задача")
    # print(page)

    page_id = Page.get_page_id_by_title("имя")
    print(page_id)


