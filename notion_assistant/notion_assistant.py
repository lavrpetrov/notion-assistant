# notion_assistant.py


from pathlib import Path
from datetime import datetime
from time import sleep
from notion.client import NotionClient
from notion.block.basic import *


token_path = Path('C:/Users/Роман/Documents/GitHub/notion-assistant') / 'config' / 'notion.token'
token = token_path.read_text().strip()

# Obtain the `token_v2` value by inspecting your browser
# cookies on a logged-in (non-guest) session on Notion.so
client = NotionClient(token_v2=token)

# Replace this URL with the URL of the page you want to edit
block_url = "https://www.notion.so/Test_Page-a15d04aee2dc49a88ca287e30ed71cb8"
page = client.get_block(block_url)

current_time = datetime.now()

while True:
    subPage = page.children.add_new(TextBlock, title = f"**Note from {current_time.strftime('%d %b %Y / %H:%M')}:**")
    sleep(10)


# for child in page.children:
#     print(f"Parent of {child.id} is {child.parent.id}")

# print(f"Parent of {page.id} is {page.parent.id}")

# print(page.get())
