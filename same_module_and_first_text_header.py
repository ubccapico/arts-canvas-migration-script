import init
import api_calls as api
import pprint


def same_module_text_header():
    modules = api.get_all_modules()
    for module in modules:
        items = api.get_module_items(module['id'])
        module_name = module['name']
        first_item_title = items[0]['title']
        first_item_type = items[0]['type']
        if first_item_title == module_name and first_item_type == 'SubHeader':
            print('We are deleting the first Text Header, "' + first_item_title + '" in the Module, "' + module_name +'"')
            api.delete_module_item(module['id'], items[0]['id'])
        if first_item_title == module_name and first_item_type == 'Page':
            print('We are deleting the first Page, "' + first_item_title + '" in the Module, "' + module_name +'"')
            api.delete_module_item(module['id'], items[0]['id'])
    print('Done deleting same Text Header or Page to Module!')