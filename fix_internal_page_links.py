from bs4 import BeautifulSoup
import unidecode
import urllib

import init
import api_calls as api


def fix_internal_page_links(page_url_html_list):

    print(page_url_html_list)

    pages = api.get_all_pages()

    # loop through every page
    for page in pages:
        body = api.get_page(page['url'])['body']
        a_tag_flag = False
        if body is not None:
            print('Fixing internal page links in {}'.format(page['title']))
            soup = BeautifulSoup(body, "html.parser")

            # Looping through a tags
            a_tags = soup.findAll('a', href=True)
            if a_tags:
                for a_tag in a_tags:
                    print('We are currently looking at the a_tag:' +
                          str(a_tag)
                          + ' which is in the page: ' + page['title'])
                    # check every page
                    decoded_href = urllib.parse.unquote(a_tag['href'].replace("+", "%20"))
                    
                    for page_url_html in page_url_html_list:
                        # see if the text within the a_tag
                        # can match the url of a page
                        a_tag_text_to_url = unidecode.unidecode(
                            a_tag.get_text().replace(' ', '-').lower())
                        if (page_url_html.html in decoded_href or
                                a_tag_text_to_url == page_url_html.url):
                            print('This a_tag: ' + decoded_href +
                                  ' matches the page: ' + page_url_html.url)
                            a_tag['href'] = init.base_url + "/courses/{}/pages/{}".format(
                                                init.course_id,
                                                page_url_html.url)
                            a_tag_flag = True

            if a_tag_flag:
                api.update_page_body(page['url'], str(soup))
                print("Some revisions were made to ({}).".format(
                    page['title']))
    return
