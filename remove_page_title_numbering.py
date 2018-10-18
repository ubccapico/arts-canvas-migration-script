import init
import api_calls as api
import pprint
import re


def remove_page_title_numbering():
    pages = api.get_all_pages()
    pattern = re.compile(r"-[\d]+$")

    for page in pages:
        page_title = page['title']
        page_url = page['url']
        match = re.search(pattern, page_title)
        if match:
            relevant_regex = str(match.group())
            relevant_number = relevant_regex.replace('-', '')
            spacing = ''
            for x in range(int(relevant_number)):
                spacing = spacing + ' '
            fixed_page_title = re.sub(pattern, spacing, page_title)
            print(page_title + ' has numbering: ' + relevant_number)
            print('Changing ' + page_title + ' to ' + fixed_page_title)
            api.update_page_title(page_url, fixed_page_title)
        else:
            print(page_title + ' does not have numbering')