properties = {"URL":{"id":"Varq","type":"url","url":{}},"Content":{"id":"pN?U","type":"rich_text","rich_text":{}},"Tags":{"id":"pk:<","type":"multi_select","multi_select":{"options":[]}},"Column":{"id":"rhr\\","type":"rich_text","rich_text":{}},"Name":{"id":"title","type":"title","title":{}}}

for key in properties:
    print(key, properties[key])
    type_column = properties[key]['type']

    for i in properties[key]:

        if i == 'title' or i == 'rich_text':
            properties[key][i].setdefault("content", '')
            properties[key][i]['content'] = 'my_testing_text'
            print(properties[key][i]['content'])
            print(properties[key][i])
