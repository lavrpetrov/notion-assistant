# notion_assistant.py


from pathlib import Path
from notion.client import NotionClient
from notion.block.basic import *


token_path = Path('C:/Users/Роман/Documents/GitHub/notion-assistant') / 'config' / 'notion.token'
token = token_path.read_text().strip()

# Obtain the `token_v2` value by inspecting your browser
# cookies on a logged-in (non-guest) session on Notion.so
client = NotionClient(token_v2=token)

# Replace this URL with the URL of the page you want to edit
block_url = "https://www.notion.so/Such-deals2-44f62260b7894844ac72a4f3a182bb7c"
page = client.get_block(block_url)


url = page.get_browseable_url
print(url)

subPage = page.children.add_new(PageBlock, title = 'new_page')

for child in page.children:
    print(f"Parent of {child.id} is {child.parent.id}")

print(f"Parent of {page.id} is {page.parent.id}")

print(page.get())
