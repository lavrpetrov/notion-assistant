from pathlib import Path

path = '/home/roman/Programming/GitHub/personal-notion-bot/.secret/'

BOT_TOKEN = Path(path + 'telegram.token').read_text().strip()

ADMIN_ID = Path(path + 'admin.id').read_text().strip()

NOTION_TOKEN = Path(path + 'notion.token').read_text().strip()

DATABASE_ID = Path(path + 'database.id').read_text().strip()
