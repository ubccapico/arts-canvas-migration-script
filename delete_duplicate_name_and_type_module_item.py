import init
import api_calls as api
import pprint

def delete_dup_name_and_type():
	all_modules = api.get_all_modules()
	for module in all_modules:
		no_dup_item_arr = []
		all_items = api.get_module_items(module['id'])
		for item in all_items:
			filtered_item = {}
			filtered_item['title'] = item['title']
			filtered_item['type'] = item['type']
			if filtered_item not in no_dup_item_arr:
				no_dup_item_arr.append(filtered_item)
			else:
				print('Deleting a duplicate item, "' + item['title'] + '", in module, "' + module['name'] + '"')
				api.delete_module_item(module['id'],item['id'])
