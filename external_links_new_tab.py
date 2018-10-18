import init
import api_calls as api
import pprint


def external_links_new_tab():
    modules = api.get_all_modules()
    for module in modules:
        print('Traversing Module: {}'.format(module['name']))
        items = api.get_module_items(module['id'])
        for item in reversed(items):
            if item['type'] == 'ExternalUrl':
                api.external_link_new_tab_api(module['id'], item['id'])
                print('The external link ' +
                      item['title'] +
                      ' now loads in a new tab.')
    print('Done running External Links to New Tabs!')
