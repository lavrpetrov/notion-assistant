from time import sleep

from loader import dispatcher
from notion_side.notion_objects import Page
from hashtags import dict_of_hashtags, templates


@dispatcher.message_handler(commands=["start", "help"])
async def helping(message):
    await message.reply(
        '''
        Привет, моя задача - создавать новые странички в Notion
        
        Чтобы создать новую страничку тебе нужно
        отправить мне сообщение, следующего формата:
        
        1. в первой строке указать все необходимые хэштеги 
           (если их нет, переходи сразу к пункту 2)
           
        2. во второй строке написать название странички
           (или в первой, если отсутствуют хэштеги)
           
        3. в оставшихся строках ты можешь написть
           то, что будет отображено внутри страницы
        
        Список поддерживаемых хэштегов^*:
        
        "Тип" -
        #покупка(#покупки, #купить, #п),
        #задача(#task, #з), #проект, #нз(#н)^**
        
        "Приоритет" -
        #высший(#5, #наивысший), #высокий(#4),
        #средний(#3), #низкий(#2), #наименьший(#1)
        
        "Срочность" -
        #срочно, #несрочно, #эксперимент,
        #хотелки, #потом
        
        "Департамент" -
        #прога, #продуктивность, #асана,
        #менеджмент, #вечеринки, #школа, #тимлидинг
        
        Значения по умолчанию^***:
        
        "Тип" - #нз
        "Приоритет" - #неназначен
        "Срочность" - #хотелки
        "Департамент" - не заполняется
        
        --------------------------------
        * - в скобках указаны синонимы
        ** - эти хэштеги для создания "Независимой задачи"
        *** - значения колонок, если какой-либо хэштег
              не указан
        '''
    )


@dispatcher.message_handler(content_types=["text"])
async def post_text(message):
    message_text = message.text
    first_string = message_text.split('\n')[0]
    list_of_hashtags = message_text.split('\n')[0].split(' ')

    page = Page

    if '#' not in first_string:
        page.make_streaming_task()

        title = first_string

        content = message_text.split('\n', 1)[-1]

    else:
        for hashtag in list_of_hashtags:
            if hashtag in templates["purchase"]:
                page.make_purchase()
            elif hashtag in templates["task"]:
                page.make_task()
            elif hashtag in templates["streaming_task"]:
                page.make_streaming_task()
            elif hashtag in templates["project"]:
                page.make_project()

        for hashtag in list_of_hashtags:
            for key in dict_of_hashtags:
                for item in dict_of_hashtags[key]:
                    if hashtag == item:
                        page.make_select(dict_of_hashtags[key][item], key)

        title = message_text.split('\n')[1]
        content = message_text.split('\n', 2)[-1]

    page.make_title(title)
    page.add_children(content)
    print(page.data_post)
    page.post_page()
    sleep(4)
    await message.reply(Page.get_page_url_by_title(title))
