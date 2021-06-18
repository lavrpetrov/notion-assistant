import os

BOT_TOKEN = os.getenv('BOT_TOKEN')

NOTION_TOKEN = os.getenv('NOTION_TOKEN')

DATABASE_ID = os.getenv('DATABASE_ID')

HEADERS = {
        'Authorization': f"Bearer {NOTION_TOKEN}",
        'Content-Type': 'application/json',
        'Notion-Version': '2021-05-13'
}

