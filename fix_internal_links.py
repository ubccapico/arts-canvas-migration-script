import urllib
from bs4 import BeautifulSoup

import api_calls as api
import init

previewable_types = ['doc', 'odt', 'sxi', 'docx', 'pdf', 'sxw', 'odf',
                     'ppt', 'xlsx', 'odg', 'pptx', 'xls', 'odp', 'rtf',
                     'txt', 'ods', 'sxc', 'mp4', 'mp3', 'ogg', 'mpeg', 'mov', 
                     'gif']


def fix_internal_links():
    print('Preparing to fix Page to File/Image Links...')
    pages = api.get_all_pages()
    images = api.get_all_files("image")
    files = api.get_all_files("")

    for page in pages:
        print('Fixing internal links in {}'.format(page['title']))
        body = api.get_page(page['url'])['body']
        # print(body.decode('utf-8'))
        image_flag, file_flag = 0, 0
        if body is not None:

            soup = BeautifulSoup(body, "html.parser")
            a_tags = soup.findAll('a', href=True)
            if a_tags:
                for a_tag in a_tags:
                    # Loop through all files looking for matches between href
                    # and file display name                    
                    decoded_href = urllib.parse.unquote(a_tag['href'].replace("+", "%20"))
                    for file in files:
                        if file['display_name'] in decoded_href:
                            print("Match(file) - {}".format(
                                file['display_name']))
                            file_flag = 1
                            for type in previewable_types:
                                if type in file['content-type']:
                                    a_tag['class'] = "instructure_file_link " \
                                                    "instructure_scribd_file"
                            a_tag['href'] = init.base_url + "/courses/{}/files/{}/download".format(
                                    init.course_id,
                                    file['id'])
                            a_tag['title'] = file['display_name']

            image_tags = soup.findAll('img', src=True)
            if image_tags:
                for img in image_tags:

                    decoded_image = urllib.parse.unquote(img['src'])
                    for image in images:
                        if image['display_name'] in decoded_image:
                            print("Match(Image) - {}".format(
                                image['display_name']))
                            image_flag = 1
                            img['src'] = init.base_url + "/courses/{}/files/{}/preview".format(
                                    init.course_id,
                                    image['id'])

            source_tags = soup.findAll('source', src=True)
            if source_tags:
                for source in source_tags:
                    decoded_image = urllib.parse.unquote(source['src'])
                    for file in files:
                        if file['display_name'] in decoded_image:
                            print(
                                "Match(Source) - {}".format(
                                    file['display_name']))
                            image_flag = 1
                            source['src'] = init.base_url + "/courses/{}/files/{}/preview".format(
                                    init.course_id,
                                    file['id'])

            audio_tags = soup.findAll('audio', src=True)
            if audio_tags:
                for audio in audio_tags:
                    decoded_audio = urllib.parse.unquote(audio['src'])
                    for file in files:
                        if file['display_name'] in decoded_audio:
                            print(
                                "Match(Audio) - {}".format(
                                    file['display_name']))
                            image_flag = 1
                            audio['src'] = init.base_url + "/courses/{}/files/{}/preview".format(
                                    init.course_id,
                                    file['id'])

            body = str(soup)

            if file_flag == 1 or image_flag == 1:
                api.update_page_body(page['url'], body)
                print("Some revisions were made to ({}).".format(
                    page['title']))
    print('Done Fixing Page to File/Image Links!')
    return
