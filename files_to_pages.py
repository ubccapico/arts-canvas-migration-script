import html
import urllib
import pprint
import os

from bs4 import BeautifulSoup, Doctype
from fix_internal_page_links import fix_internal_page_links
from fix_internal_links import fix_internal_links

import api_calls as api
import urllib.request as req
import init

page_url_html_list = []


# class to hold PageUrlHtml elements
class PageUrlHtml(object):
    def __init__(self, url, html):
        self.url = url
        self.html = html

    def __repr__(self):
        return str(self.__dict__)


def delete_all_html_files():
    print('Now deleting all HTML files in course...')
    all_html_files = api.get_all_files('text/html')
    file_count = 0
    for file in all_html_files:
        api.delete_file(file['id'])
        print('Deleted converted HTML file: ' + file['display_name'])
        file_count += 1
    print(str(file_count) + " HTML files were deleted.")
    return


# converts files to pages
def ftp(module_ID, position, indent, file_url, filename, title, item_ID):
    # download file contents into html_content string
    response = req.urlopen(file_url)
    html_raw = html.unescape(response.read().decode('utf-8', 'replace'))
    response.close()

    soup = BeautifulSoup(html_raw, "html.parser")

    # removes doctype
    for item in soup.contents:
        if isinstance(item, Doctype):
            item.extract()

    head_html = soup.find('head')
    if head_html:
        head_html.extract()
    # fix tables tags to have borders
    tables = soup.findAll('table', border=None)
    if tables is not None:
        for table in tables:
            table['border'] = "1"
    # fix audio tags to have no styling
    audios = soup.findAll('audio')
    if audios is not None:
        for audio in audios:
            audio['style'] = ""
    body = str(soup)

    # titles cannot be periods, replace with asterisk
    if title == '.' or title == '&nbsp;':
        title = '*'
    try:
        page = api.create_page(title, body)
        decoded_filename = urllib.parse.unquote(filename.replace("+", "%20"))
        page_url_html_list.append(PageUrlHtml(page['url'], decoded_filename))
        added_page = api.add_page_to_module(
            module_ID,
            page['url'],
            position,
            indent)
        api.delete_module_item(module_ID, item_ID)
        api.publish_module_item(module_ID, added_page['id'])

        print('Converted - ' + str(title))
    except Exception as e:
        print('Could not convert - ' + str(title))
    return

# checks if the module item is HTML


def ftp_if_html(module_ID, item):
    if (item['type'] == 'File'):
        file = api.get_file(item['content_id'])
        if (file['content-type'] == 'text/html'):
            ftp(module_ID=module_ID,
                position=item['position'],
                indent=item['indent'],
                file_url=file['url'],
                filename=file['filename'],
                title=item['title'],
                item_ID=item['id'])
        else:
            api.publish_module_item(module_ID, item['id'])
    else:
        api.publish_module_item(module_ID, item['id'])
    return


# loops through items in module
def traverse_module_ftp(module_ID):
    # get get all module items in a list. For each item, call ftp_if_html
    items = api.get_module_items(module_ID)
    for item in reversed(items):
        ftp_if_html(module_ID, item)
    return

# loops through modules


def traverse_course_ftp():
    #    get all modules (Module ID) into an array
    #    call traverse module on each module
    modules = api.get_all_modules()
    for module in modules:
        print('Traversing Module: {}'.format(module['name']))
        traverse_module_ftp(module['id'])
    return


def traverse_files_ftp():
    html_files = api.get_all_files('text/html')
    for html in html_files:
        found = False
        for page_url_html in page_url_html_list:
            if html['filename'] == page_url_html.html:
                found = True
                break
        if(found is False):
            create_page_from_file(html)


def create_page_from_file(file):
    file_url = file['url']
    file_uuid = file['uuid']
    title = file['display_name']
    title_no_extension = os.path.splitext(title)[0]
    filename = file['filename']
    response = req.urlopen(file_url)
    html_raw = html.unescape(response.read().decode('utf-8', 'replace'))
    response.close()

    soup = BeautifulSoup(html_raw, "html.parser")

    # removes doctype
    for item in soup.contents:
        if isinstance(item, Doctype):
            item.extract()

    head_html = soup.find('head')
    if head_html:
        head_html.extract()
    # fix tables tags to have borders
    tables = soup.findAll('table', border=None)
    if tables is not None:
        for table in tables:
            table['border'] = "1"
    # fix audio tags to have no styling
    audios = soup.findAll('audio')
    if audios is not None:
        for audio in audios:
            audio['style'] = ""
    body = str(soup)

    # titles cannot be periods, replace with asterisk
    if title == '.' or title == '&nbsp;':
        title = '*'
        title_no_extension = '*'
    try:
        page = api.create_page(title_no_extension, body)
        decoded_filename = urllib.parse.unquote(filename.replace("+", "%20"))
        page_url_html_list.append(PageUrlHtml(page['url'], decoded_filename))
        page_url_html_list.append(PageUrlHtml(page['url'], file_uuid))
        print('Converted - ' + str(title))
    except Exception as e:
        print('Could not convert - ' + str(title))
    return


# master function called for ftp

def master_ftp():
    print('****FILES TO PAGES********')
    print('Starting to convert HTMLs to Pages in Modules')
    traverse_course_ftp()
    print('Starting to convert HTMLs to Pages in Files')
    traverse_files_ftp()
    print('Starting to fix page to page links')
    fix_internal_page_links(page_url_html_list)
    print('Starting to fix page to file/image links')
    fix_internal_links()
    print('Starting to delete the converted HTML files...')
    delete_all_html_files()
    print("Done running Files to Pages!")
    return
