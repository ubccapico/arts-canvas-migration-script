import init
import api_calls as api
import pprint

def publish_all():
    item_array = []
    modules = api.get_all_modules()
    for module in modules:
        if module['published'] is not True:
            api.publish_module(module['id'])
            print('Publishing module: ' + module['name'])
        items = api.get_module_items(module['id'])
        for item in items:
            if item['published'] is not True:
                api.publish_module_item(module['id'], item['id'])
                print('Publishing module item: ' + item['title'])
