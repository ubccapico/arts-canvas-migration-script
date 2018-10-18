import requests
import json
import init
from decimal import Decimal



def delete_component(course_id,
                     token,
                     to_be_deleted,
                     ids,
                     to_be_deleted_full_json):

    print("Deleting " + to_be_deleted + "...")

    percent_complete = 0
    total_num = 0

    if to_be_deleted == "pages":
        blank_page = requests.post(
            url + '/api/v1/courses/' + course_id + '/pages/',
            headers={'Authorization': 'Bearer ' + token},
            data={'wiki_page[title]': 'Blank Page (for FrontPage trigger)',
                  'wiki_page[published]': 'True',
                  'wiki_page[front_page]': 'True'})

    if to_be_deleted == "announcements":
        to_be_deleted_items = requests.get(
            url + '/api/v1/courses/' + course_id + '/discussion_topics/',
            headers={'Authorization': 'Bearer ' + token},
            data={'only_announcements': 'True', 'per_page': 100})

    else:
        to_be_deleted_items = requests.get(
            url + '/api/v1/courses/' + course_id + '/' + to_be_deleted + '/',
            headers={'Authorization': 'Bearer ' + token})

    print("Calculating how many " + to_be_deleted +
          " are there to be deleted...\n")

    while True:
        to_be_deleted_items_json = json.loads(to_be_deleted_items.text)
        to_be_deleted_full_json += to_be_deleted_items_json

        num = len(to_be_deleted_items_json)
        total_num += num

        for x in range(num):
            if (to_be_deleted == "discussion_topics" or
                    to_be_deleted == "quizzes" or
                    to_be_deleted == "announcements"):

                ids[to_be_deleted_items_json[x][u'id']
                    ] = to_be_deleted_items_json[x][u'title']

            elif to_be_deleted == "files":
                ids[to_be_deleted_items_json[x][u'id']
                    ] = to_be_deleted_items_json[x][u'display_name']

            elif to_be_deleted == "pages":
                ids[to_be_deleted_items_json[x][u'url']
                    ] = to_be_deleted_items_json[x][u'title']

            else:
                ids[to_be_deleted_items_json[x][u'id']
                    ] = to_be_deleted_items_json[x][u'name']

        if (to_be_deleted_items.links['current']['url']
                == to_be_deleted_items.links['last']['url']):
            break

        else:
            to_be_deleted_items = requests.get(
                to_be_deleted_items.links['next']['url'],
                headers={'Authorization': 'Bearer ' + token})

    if total_num == 0:
        print("There are no " + to_be_deleted + " to be deleted\n")

    else:
        print("There are " + str(total_num) + " of " +
              to_be_deleted + " to be deleted")

        percent_inc = round(Decimal(100.0 / total_num), 2)
        print('The percentage increment is: ' + str(percent_inc))

        for x in ids.keys():
            if to_be_deleted == "announcements":
                to_be_deleted_items = requests.get(
                    url + '/api/v1/courses/'
                        + course_id
                        + '/discussion_topics/',
                    headers={'Authorization': 'Bearer ' + token},
                    data={'only_announcements': 'True'})
            else:
                to_be_deleted_items = requests.get(
                    url + '/api/v1/courses/'
                        + course_id + '/'
                        + to_be_deleted
                        + '/'
                        + str(x),
                    headers={'Authorization': 'Bearer ' + token})

            to_be_deleted_items_json = json.loads(to_be_deleted_items.text)

            if to_be_deleted == "files" or to_be_deleted == "folders":
                to_be_deleted_items = requests.delete(
                    url + '/api/v1/'
                        + '/'
                        + to_be_deleted
                        + '/'
                        + str(x),
                    headers={'Authorization': 'Bearer ' + token},
                    data={'force': 'True'})
            elif to_be_deleted == "announcements":
                to_be_deleted_items = requests.delete(
                    url + '/api/v1/courses/'
                        + course_id
                        + '/discussion_topics/'
                        + str(x),
                    headers={'Authorization': 'Bearer ' + token},
                    data={'only_announcements': 'True'})
            else:
                to_be_deleted_items = requests.delete(
                    url + '/api/v1/courses/'
                        + course_id
                        + '/'
                        + to_be_deleted
                        + '/'
                        + str(x),
                    headers={'Authorization': 'Bearer ' + token})

            percent_complete += percent_inc

            print(str(percent_complete) + "% Complete!")

    print("All " + to_be_deleted + " have now been deleted\n")


def delete_syllabus(course_id,
                    token):

    course = requests.get(url + '/api/v1/courses/' + course_id,
                          headers={'Authorization': 'Bearer ' + token})
    course_json = json.loads(course.text)

    delete_syllabus = requests.put(url + '/api/v1/courses/' + course_id,
                                   headers={
                                       'Authorization': 'Bearer ' + token},
                                   data={'course[syllabus_body]': ''})

    print("Finished deleting the Syllabus")


def reset_navigation(course_id,
                     token):

    tabs_visible = ['Discussions',
                    'Grades',
                    'People',
                    'Syllabus',
                    'My Media',
                    'Media Gallery',
                    'Chat',
                    'CoursEval']

    tabs_hidden = ['Announcements',
                   'Assignments',
                   'Pages',
                   'Files',
                   'Outcomes',
                   'Quizzes',
                   'Modules']

    all_tabs = tabs_hidden[0:2] + tabs_visible[1:4] + tabs_hidden[2:5] + \
        ['Syllabus'] + tabs_hidden[4:7] + tabs_visible[5:10]

    course_tabs = requests.get(url + '/api/v1/courses/' + course_id + '/tabs',
                               headers={'Authorization': 'Bearer ' + token})

    course_tabs_json = json.loads(course_tabs.text)

    total_tabs = len(course_tabs_json)

    for x in range(total_tabs):
        ids[course_tabs_json[x][u'id']] = course_tabs_json[x][u'label']

    for x in ids.keys():
        if ids[x] not in tabs_visible:
            course_tabs = requests.put(
                url + '/api/v1/courses/'
                    + course_id
                    + '/tabs/'
                    + str(x),
                headers={'Authorization': 'Bearer ' + token},
                data={'hidden': 'True'})
        try:
            course_tabs = requests.put(
                url + '/api/v1/courses/'
                    + course_id
                    + '/tabs'
                    + str(x),
                headers={'Authorization': 'Bearer ' + token},
                data={'position': (all_tabs.index(ids[x]) + 1)})
        except ValueError:
            course_tabs = requests.put(
                url + '/api/v1/courses/'
                    + course_id
                    + '/tabs'
                    + str(x),
                headers={'Authorization': 'Bearer ' + token},
                data={'hidden': 'True'})

    print("Navigation for the course has been reset\n")


def delete_course():
    global url
    global ids
    url = init.base_url
    continue_prompt = "n"
    undo = "n"
    ids = {}
    to_be_deleted_full_json = []
    all_tabs = []
    total_num = 0
    components_to_be_deleted = ['announcements',
                                'discussion_topics',
                                'quizzes',
                                'modules',
                                'assignments',
                                'assignment_groups',
                                'groups',
                                'files',
                                'folders',
                                'pages',
                                'external_tools']

    token = init.access_token
    course_id = init.course_id

    for to_be_deleted in components_to_be_deleted:

        delete_component(course_id,
                         token,
                         to_be_deleted,
                         ids,
                         to_be_deleted_full_json)
        ids = {}
        print("Finished with " + to_be_deleted + "\n")

    delete_syllabus(course_id,
                    token)

    reset_navigation(course_id,
                     token)

    requests.put(url + '/api/v1/courses/' + course_id,
                 headers={'Authorization': 'Bearer ' + token},
                 data={'offer': 'False'})

    print("Done")
