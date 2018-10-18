import init
import api_calls as api
import pprint


def get_all_items():
    item_array = []
    modules = api.get_all_modules()
    for module in modules:
        module['type'] = 'module'
        item_array.append(module)
        items = api.get_module_items(module['id'])
        for item in items:
            item['type'] = 'item'
            item_array.append(item)
    return item_array


def get_all_modules():
    module_array = []
    modules = api.get_all_modules()
    return modules


def mass_move(module_id_dest, itemArray):
    for item in reversed(itemArray):
        print('Moving ' + item.item_title)
        api.move_item(item.item_id, item.item_module_id, module_id_dest)
