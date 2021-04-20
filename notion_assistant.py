# notion-assistant.py


from pathlib import Path
from notion.client import NotionClient
from notion.block.basic import *


secret = Path('C:\\Users\Роман\\Documents\\my_secret\\secret.txt').read_text().strip()

# Obtain the `token_v2` value by inspecting your browser
# cookies on a logged-in (non-guest) session on Notion.so
client = NotionClient(token_v2=secret)

# Replace this URL with the URL of the page you want to edit
page = client.get_block("https://www.notion.so/Such-deals2-44f62260b7894844ac72a4f3a182bb7c")


url = page.get_browseable_url
print(url)

subPage = page.children.add_new(PageBlock, title = 'new_page')

for child in page.children:
    print(f"Parent of {child.id} is {child.parent.id}")

print(f"Parent of {page.id} is {page.parent.id}")

print(page.get())
