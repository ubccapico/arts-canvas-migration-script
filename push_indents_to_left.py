import init
import api_calls as api
import pprint


def get_all_items():
    item_array = []
    modules = api.get_all_modules()
    for module in modules:
        item_array.append(module)
        items = api.get_module_items(module['id'])
        for item in items:
            item_array.append(item)
    return item_array


def get_all_modules():
    module_array = []
    modules = api.get_all_modules()
    return modules


def push_indents_to_left():
    modules = api.get_all_modules()
    for module in modules:
        items = api.get_module_items(module['id'])
        item_indent_array = []
        for item in items:
            item_indent_array.append(item['indent'])
        if len(item_indent_array) > 0:
            m = min(i for i in item_indent_array if i >= 0)
            for item in items:
                if m > 0:
                    print('Currenting decreasing indent on "' + item['title'] + '"')
                    for _ in range(m):
                        api.decrease_indent(module['id'], item['id'])