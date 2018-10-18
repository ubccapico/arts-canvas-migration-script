import requests
import json
import init
import pprint

import init
import api_calls as api

all_folders = []


def get_more_folders(links):
    if 'next' in links:
        more_folders = requests.get(links['next']['url'], params={'access_token': init.access_token})
        global all_folders
        all_folders = all_folders + more_folders.json()
        get_more_folders(more_folders.links)

def master_delete_empty_modules():
    all_modules = api.get_all_modules()
    for module in all_modules:
        if module['items_count'] == 0:
            deleted_empty_module = api.delete_module(module['id'])
            print('Deleted empty module: ' + deleted_empty_module['name'])


def get_all_folders():
    folders = requests.get(
        init.base_url + '/api/v1/courses/{}/folders'.format(
            str(init.course_id)),
        params={'access_token': init.access_token, 'per_page': 100})
    global all_folders
    all_folders = all_folders + folders.json()
    more_folders = get_more_folders(folders.links)


def delete_folder(folder_id):
    delete_folder_url = init.base_url + '/api/v1/folders/' + folder_id
    deleted_folder = requests.delete(
        delete_folder_url,
        params={
            'access_token': init.access_token})


def master_delete_folder():
    global all_folders
    all_folders = []
    get_all_folders()
    while any(folder['folders_count'] is 0 and folder['files_count'] is 0 for folder in all_folders):
        for folder in all_folders:
            if folder['folders_count'] is 0 and folder['files_count'] is 0:
                print('Deleting empty folder: ' + folder['name'])
                delete_folder(str(folder['id']))
        master_delete_folder()



def delete_announcements(course_id,
                         token,
                         announcement_ids,
                         announcements_full_json):

    print("Deleting announcements...")

    percent_complete = 0
    total_num = 0

    announcement_items = requests.get(
        url + '/api/v1/courses/'
            + course_id
            + '/discussion_topics/',
        headers={'Authorization': 'Bearer ' + token},
        data={'only_announcements': 'True'})

    print("Calculating how many announcements are there to be deleted...\n")

    while True:
        announcement_items_json = json.loads(announcement_items.text)
        announcements_full_json += announcement_items_json

        num = len(announcement_items_json)
        total_num += num

        for x in range(num):
            announcement_ids[announcement_items_json[x][u'id']
                             ] = announcement_items_json[x][u'title']

        if (announcement_items.links['current']['url']
                == announcement_items.links['last']['url']):
            break

        else:
            announcement_items = requests.get(
                announcement_items.links['next']['url'],
                headers={'Authorization': 'Bearer ' + token},
                data={'only_announcements': 'True'})

    if total_num == 0:
        print("There are no announcements to be deleted\n")

    else:
        print("There are " + str(total_num) + " announcements to be deleted")

        percent_inc = int(100.0 / total_num)

        for x in announcement_ids.keys():
            announcement_items = requests.get(
                url + '/api/v1/courses/'
                    + course_id
                    + '/discussion_topics/'
                    + str(x),
                headers={'Authorization': 'Bearer ' + token})

            announcement_items_json = json.loads(announcement_items.text)
            percent_complete += percent_inc

            print(str(percent_complete) + "% Complete. Announcement titled: " +
                  announcement_items_json[u'title'] + " Deleted!")

            announcement_items = requests.delete(
                url + '/api/v1/courses/'
                    + course_id
                    + '/discussion_topics/'
                    + str(x),
                headers={'Authorization': 'Bearer ' + token})

        print("All announcements have now been deleted\n")


def delete_assignment_groups(course_id,
                             token,
                             assignment_group_ids,
                             assignment_group_full_json):

    print("Deleting empty assignment groups...")

    percent_complete = 0
    total_num = 0
    assignment_titles_to_be_deleted = ["Program",
                                       "Majors",
                                       "Year Level",
                                       "Faculty",
                                       "Minors",
                                       "Term",
                                       "Linked Section",
                                       "Discussion", "Lab",
                                       "Program Year",
                                       "Section",
                                       "Status",
                                       "Tutorial"]

    assignment_group_items = requests.get(
        url + '/api/v1/courses/'
            + course_id
            + '/assignment_groups/',
        headers={'Authorization': 'Bearer ' + token},
        data={'include': 'assignments'})

    print("Calculating how many " +
          "assignment groups are there to be deleted...\n")

    while True:
        assignment_group_items_json = json.loads(assignment_group_items.text)
        assignment_group_full_json += assignment_group_items_json

        num = len(assignment_group_items_json)
        print('The length of the assignment group items is: ' + str(num))

        for x in range(num):
            num_of_assignments = len(
                assignment_group_items_json[x][u'assignments'])
            assignment_group_id = assignment_group_items_json[x][u'id']

            if (num_of_assignments == 0):
                assignment_group_ids[assignment_group_items_json[x]
                                     [u'id']] = assignment_group_items_json[x][u'name']

        if (assignment_group_items.links
                ['current']['url'] == assignment_group_items.links
                ['last']['url']):
            break

        else:
            assignment_group_items = requests.get(
                assignment_group_items.links['next']['url'],
                headers={'Authorization': 'Bearer ' + token},
                data={'include': 'assignments'})

    total_num = len(assignment_group_ids)

    if total_num == 0:
        print("There are no assignment groups to be deleted\n")

    else:
        print("There are " + str(total_num) +
              " assignment groups to be deleted")

        percent_inc = int(100.0 / total_num)

        for x in assignment_group_ids.keys():
            assignment_group_items = requests.get(
                url + '/api/v1/courses/'
                    + course_id
                    + '/assignment_groups/'
                    + str(x),
                headers={'Authorization': 'Bearer ' + token},
                data={'include': 'assignments'})

            assignment_group_items_json = json.loads(
                assignment_group_items.text)
            percent_complete += percent_inc

            print(str(percent_complete)
                  + "% Complete. Assignment Group titled " +
                  assignment_group_items_json[u'name'] + " Deleted!")

            assignment_group_items_delete = requests.delete(
                url + '/api/v1/courses/'
                    + course_id
                    + '/assignment_groups/'
                    + str(x),
                headers={'Authorization': 'Bearer ' + token})

        print("All assignment groups have been have been deleted\n")


def delete_assignments(course_id,
                       token,
                       assignment_ids,
                       assignments_full_json):

    print("Deleting unneccessary assignments...")

    percent_complete = 0
    total_num = 0
    assignment_titles_to_be_deleted = ["Program",
                                       "Majors",
                                       "Year Level",
                                       "Faculty",
                                       "Minors",
                                       "Term",
                                       "Linked Section",
                                       "Discussion",
                                       "Lab",
                                       "Program Year",
                                       "Section",
                                       "Status",
                                       "Tutorial"]

    assignments_items = requests.get(
        url + '/api/v1/courses/'
            + course_id
            + '/assignments/',
        headers={'Authorization': 'Bearer ' + token})

    print("Calculating how many assignments are there to be deleted...\n")

    while True:
        assignments_items_json = json.loads(assignments_items.text)
        assignments_full_json += assignments_items_json
        num = len(assignments_items_json)

        for x in range(num):
            if (assignments_items_json[x][u'name'] in
                    assignment_titles_to_be_deleted):
                assignment_ids[assignments_items_json[x][u'id']
                               ] = assignments_items_json[x][u'name']

        if (assignments_items.links
                ['current']['url'] == assignments_items.links
                ['last']['url']):
            break

        else:
            assignments_items = requests.get(
                assignments_items.links['next']['url'],
                headers={'Authorization': 'Bearer ' + token})

    total_num = len(assignment_ids)

    if total_num == 0:
        print("There are no assignments to be deleted\n")
    else:
        print("There are " + str(total_num) + " assignments to be deleted")
        percent_inc = int(100.0 / total_num)

        for x in assignment_ids.keys():
            assignment_items = requests.get(
                url + '/api/v1/courses/'
                    + course_id
                    + '/assignments/'
                    + str(x),
                headers={'Authorization': 'Bearer ' + token})
            assignment_items_json = json.loads(assignment_items.text)
            percent_complete += percent_inc
            print(str(percent_complete) + "% Completed. Assignment titled " +
                  assignment_items_json[u'name'] + " Deleted!")
            assignment_items_delete = requests.delete(
                url + '/api/v1/courses/'
                    + course_id
                    + '/assignments/'
                    + str(x),
                headers={'Authorization': 'Bearer ' + token})

        print("All assignment have been have been deleted\n")


def master_delete_excess():
    global url
    url = init.base_url
    global announcements_full_json
    announcements_full_json = []
    global assignment_group_full_json
    assignment_group_full_json = []
    global assignments_full_json
    assignments_full_json = []
    global announcement_ids
    announcement_ids = {}
    global assignment_group_ids
    assignment_group_ids = {}
    global assignment_ids
    assignment_ids = {}

    course_id = init.course_id
    token = init.access_token

    delete_announcements(course_id, token, announcement_ids,
                         announcements_full_json)

    delete_assignment_groups(
        course_id, token, assignment_group_ids, assignment_group_full_json)

    delete_assignments(course_id, token, assignment_ids, assignments_full_json)

    print("Starting to delete empty folders...")
    master_delete_folder()

    print('Starting to delete empty modules...')
    master_delete_empty_modules()

    print("Done Deleting Excess Content!")
