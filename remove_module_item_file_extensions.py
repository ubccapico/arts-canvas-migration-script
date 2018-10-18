import init
import api_calls as api
import pprint
import os

def remove_file_extension_from_module_items():
    file_extensions = ['.doc', '.odt', '.sxi', '.docx', '.pdf', '.sxw', '.odf', '.zip', '.imscc',
                     '.ppt', '.xlsx', '.odg', '.pptx', '.xls', '.odp', '.rtf', '.html', '.csv',
                     '.txt', '.ods', '.sxc', '.mp4', '.mp3', '.ogg', '.mpeg','.wav','.zip','.rar']
    modules = api.get_all_modules()
    for module in modules:
        items = api.get_module_items(module['id'])
        for item in items:
            old_title = item['title']
            root, ext = os.path.splitext(old_title)
            if ext in file_extensions:
                ext = ''
                new_title = root + ext 
                updated_title = api.update_module_item_name(module['id'],item['id'],new_title)
                pprint.pprint('Old title: ' + old_title)
                pprint.pprint('New title: ' + new_title)
