import requests
import init
import pprint


def get_accounts():
    accounts = requests.get(
        init.base_url + '/api/v1/accounts', params={'access_token': init.access_token})
    pprint.pprint(accounts.json())
    return accounts.json()

def get_all_subaccounts(account_id):
    page_set = []
    # initial request
    buffer100 = requests.get(
        init.base_url + '/api/v1/accounts/{}/sub_accounts'.format(str(account_id)),
        params={'access_token': init.access_token, 'per_page': 50})
    raw = buffer100.json()
    for page in raw:
        page_set.append(page)
    # return pages.json()
    while buffer100.links['current']['url'] != buffer100.links['last']['url']:
        buffer100 = requests.get(
            buffer100.links['next']['url'],
            params={'access_token': init.access_token, 'per_page': 50})
        raw = buffer100.json()
        for page in raw:
            page_set.append(page)
    return page_set

def get_all_courses():
    page_set = []
    # initial request
    buffer100 = requests.get(
        init.base_url + '/api/v1/courses',
        params={'access_token': init.access_token, 'per_page': 100})
    raw = buffer100.json()
    for page in raw:
        page_set.append(page)
    # return pages.json()
    while buffer100.links['current']['url'] != buffer100.links['last']['url']:
        buffer100 = requests.get(
            buffer100.links['next']['url'],
            params={'access_token': init.access_token, 'per_page': 100})
        raw = buffer100.json()
        for page in raw:
            page_set.append(page)
    return page_set


def get_course():
    course = requests.get(
        init.base_url + '/api/v1/courses/' + init.course_id,
        headers={'Authorization': 'Bearer ' + init.access_token})
    return course.json()


def get_all_quizzes():
    quizzes = requests.get(
        init.base_url + '/api/v1/courses/' + "{}/quizzes".format(init.course_id),
        params={'access_token': init.access_token, 'per_page': 100})
    return quizzes.json()


def get_all_files(file_type):
    file_set = []
    if file_type == '':
        parameters = {'access_token': init.access_token, 'per_page': 50}
    else:
        parameters = {'access_token': init.access_token,
                      'per_page': 50, 'content_types[]': file_type}

    # initial request
    buffer100 = requests.get(
        init.base_url + '/api/v1/courses/' + '{}/files/'.format(str(init.course_id)),
        params=parameters)
    raw = buffer100.json()
    for file in raw:
        file_set.append(file)

    while buffer100.links['current']['url'] != buffer100.links['last']['url']:
        buffer100 = requests.get(buffer100.links['next']['url'],
                                 params=parameters)
        raw = buffer100.json()
        for file in raw:
            file_set.append(file)
    return file_set


def get_all_pages():
    page_set = []
    # initial request
    buffer100 = requests.get(
        init.base_url + '/api/v1/courses/' + '{}/pages/'.format(str(init.course_id)),
        params={'access_token': init.access_token, 'per_page': 50})
    raw = buffer100.json()
    for page in raw:
        page_set.append(page)
    # return pages.json()
    while buffer100.links['current']['url'] != buffer100.links['last']['url']:
        buffer100 = requests.get(
            buffer100.links['next']['url'],
            params={'access_token': init.access_token, 'per_page': 50})
        raw = buffer100.json()
        for page in raw:
            page_set.append(page)
    return page_set


def get_all_modules():
    module_set = []
    # initial request
    buffer100 = requests.get(
        init.base_url + '/api/v1/courses/' + '{}/modules/'.format(str(init.course_id)),
        params={'access_token': init.access_token, 'per_page': 50})
    raw = buffer100.json()
    for module in raw:
        module_set.append(module)
    # return pages.json()
    while buffer100.links['current']['url'] != buffer100.links['last']['url']:
        buffer100 = requests.get(
            buffer100.links['next']['url'],
            params={'access_token': init.access_token, 'per_page': 50})
        raw = buffer100.json()
        for module in raw:
            module_set.append(module)
    return module_set


def set_home():
    home = requests.put(
        init.base_url + '/api/v1/courses/' + init.course_id,
        params={
            'access_token': init.access_token,
            'course[default_view]': 'syllabus'})
    return home.json()


def start_link_validation():
    start = requests.post(
        init.base_url + '/api/v1/courses/' + '{}/link_validation'.format(init.course_id),
        params={
            'access_token': init.access_token,
            'course[default_view]': 'syllabus'})
    return start.json()


def get_module(module_ID):
    module = requests.get(
        init.base_url + '/api/v1/courses/' + '{}/modules/{}'.format(
            str(init.course_id),
            str(module_ID)),
        params={'access_token': init.access_token})
    return module.json()


def get_module_items(module_ID):
    item_set = []
    # initial request
    buffer100 = requests.get(
        init.base_url + '/api/v1/courses/' +
        '{}/modules/{}/items'.format(str(init.course_id), str(module_ID)),
        params={'access_token': init.access_token, 'per_page': 50})
    raw = buffer100.json()
    for item in raw:
        item_set.append(item)
    # return pages.json()
    while buffer100.links['current']['url'] != buffer100.links['last']['url']:
        buffer100 = requests.get(
            buffer100.links['next']['url'],
            params={
                'access_token': init.access_token,
                'per_page': 50})
        raw = buffer100.json()
        for item in raw:
            item_set.append(item)
    return item_set


def get_module_item(module_ID, item_ID):
    moduleItem = requests.get(
        init.base_url + '/api/v1/courses/' + '{}/modules/{}/items/{}'.format(
            str(init.course_id), str(module_ID),
            str(item_ID)),
        params={'access_token': init.access_token})
    return moduleItem.json()


def add_page_to_module(module_ID, page_url, position, indent):
    added_page = requests.post(
        init.base_url + '/api/v1/courses/' + '{}/modules/{}/items'.format(
            str(init.course_id),
            str(module_ID)),
        params={'access_token': init.access_token},
        data={'module_item[type]': 'Page',
              'module_item[page_url]': page_url,
              'module_item[position]': position,
              'module_item[indent]': indent})
    return added_page.json()


def publish_module_item(module_ID, item_ID):
    published_item = requests.put(
        init.base_url + '/api/v1/courses/' + '{}/modules/{}/items/{}'.format(
            str(init.course_id),
            str(module_ID),
            str(item_ID)),
        params={'access_token': init.access_token},
        data={'module_item[published]': True})


def publish_module(module_ID):
    published_item = requests.put(
        init.base_url + '/api/v1/courses/' + '{}/modules/{}'.format(
            str(init.course_id),
            str(module_ID)),
        params={'access_token': init.access_token},
        data={'module[published]': True})


def delete_module_item(module_ID, item_ID):
    deleted_item = requests.delete(
        init.base_url + '/api/v1/courses/' + '{}/modules/{}/items/{}'.format(
            init.course_id,
            module_ID,
            item_ID),
        params={'access_token': init.access_token})

def delete_module(module_id):
    delete_module_url = str(init.base_url) + '/api/v1/courses/'+ str(init.course_id) + '/modules/' + str(module_id)
    deleted_module = requests.delete(
        delete_module_url,
        params={
            'access_token': init.access_token})
    return deleted_module.json()

# Single Page
def get_page(page_URL):
    page = requests.get(
        init.base_url + '/api/v1/courses/' + '{}/pages/{}'.format(
            str(init.course_id),
            str(page_URL)),
        params={'access_token': init.access_token})
    return page.json()


def create_page(page_title, page_body):
    page = requests.post(
        init.base_url + '/api/v1/courses/' + "{}/pages".format(init.course_id),
        params={'access_token': init.access_token},
        data={'wiki_page[published]': 'True',
              'wiki_page[title]': page_title,
              'wiki_page[body]': page_body})
    return page.json()


def update_page_title(page_URL, title):
    page = requests.put(
        init.base_url + '/api/v1/courses/' + '{}/pages/{}'.format(
            str(init.course_id),
            str(page_URL)),
        params={'access_token': init.access_token},
        data={'wiki_page[title]': title})
    return page.json()


def update_page_body(page_URL, new_body):
    page = requests.put(
        init.base_url + '/api/v1/courses/' + '{}/pages/{}'.format(
            str(init.course_id),
            str(page_URL)),
        params={'access_token': init.access_token},
        data={'wiki_page[body]': new_body})
    return page.json()


def get_page_revisions(page_URL):
    revision = requests.get(
        init.base_url + '/api/v1/courses/' + '{}/pages/{}/revisions'.format(
            init.course_id,
            page_URL),
        params={'access_token': init.access_token})
    return revision.json()


def revert_to_page_revision(page_URL, revision_ID):
    revision = requests.post(
        init.base_url + '/api/v1/courses/' + '{}/pages/{}/revisions/{}'.format(
            init.course_id,
            page_URL,
            revision_ID),
        params={'access_token': init.access_token})
    return revision.json()


# Single File
def get_file(file_ID):
    file = requests.get(
        init.base_url + '/api/v1/courses/' + '{}/files/{}'.format(
            str(init.course_id),
            str(file_ID)),
        params={'access_token': init.access_token})
    return file.json()


def delete_file(file_ID):
    file = requests.delete(
        init.base_url + '/api/v1/' + 'files/{}'.format(
            str(file_ID)),
        params={'access_token': init.access_token})
    return file.json()


def external_link_new_tab_api(module_ID, item_ID):
    external_url_new_tab = requests.put(
        init.base_url + '/api/v1/courses/' + '{}/modules/{}/items/{}'.format(
            str(init.course_id),
            str(module_ID),
            str(item_ID)),
        params={'access_token': init.access_token},
        data={'module_item[new_tab]': True})


def move_item(item_id, item_module_id, module_dest):
    moved = requests.put(
        init.base_url + '/api/v1/courses/' + '{}/modules/{}/items/{}'.format(
            str(init.course_id),
            str(item_module_id),
            str(item_id)),
        params={'access_token': init.access_token},
        data={'module_item[module_id]': module_dest})
    moved_json = moved.json()
    new_module_id = moved_json['module_id']
    new_item_id = moved_json['id']
    new_position = moved_json['position']
    requests.put(
        init.base_url + '/api/v1/courses/' + '{}/modules/{}/items/{}'.format(
            str(init.course_id),
            str(new_module_id),
            str(new_item_id)),
        params={'access_token': init.access_token},
        data={'module_item[position]': 1})

def update_course_subaccount(account_id,subaccount_id):
    updated_course = requests.put(
        init.base_url + '/api/v1/courses/' + '{}'.format(
            str(init.course_id)),
        params={'access_token': init.access_token},
        data={'course[account_id]': subaccount_id})
    return updated_course.json()



def update_course_name(name):
    course_code = requests.put(
        init.base_url + '/api/v1/courses/' + '{}'.format(
            str(init.course_id)),
        params={'access_token': init.access_token},
        data={'course[name]': name})


def update_course_code(code):
    course_code = requests.put(
        init.base_url + '/api/v1/courses/' + '{}'.format(
            str(init.course_id)),
        params={'access_token': init.access_token},
        data={'course[course_code]': code})


def decrease_indent(module_id, item_id):
        item = requests.get(
            init.base_url + '/api/v1/courses/' + '{}/modules/{}/items/{}'.format(
                str(init.course_id),
                str(module_id),
                str(item_id)),
            params={'access_token': init.access_token})

        item = item.json()

        requests.put(
            init.base_url + '/api/v1/courses/' + '{}/modules/{}/items/{}'.format(
                str(init.course_id),
                str(module_id),
                str(item_id)),
            params={'access_token': init.access_token},
            data={'module_item[indent]': item['indent'] - 1})


def create_new_module(module_name):
    new_module = requests.post(
        init.base_url + '/api/v1/courses/' + '{}/modules/'.format(
            str(init.course_id)),
        params={'access_token': init.access_token},
        data={'module[name]': module_name})

def create_new_modules(module_name_array):
    for module_name in module_name_array:
        new_module = requests.post(
            init.base_url + '/api/v1/courses/' + '{}/modules/'.format(
                str(init.course_id)),
            params={'access_token': init.access_token},
            data={'module[name]': module_name})


def fix_question(quiz_id, question_id):
    fixed_question = requests.post(
        init.base_url + '/api/v1/courses/' + '{}/quizzes/{}/reorder'.format(
            str(init.course_id),
            str(quiz_id)),
        params={'access_token': init.access_token},
        data={'order[][id]': question_id,
              'order[][type]': 'question'})


def fix_question_points(quiz_id, question_id, points):
    fixed_question = requests.put(
        init.base_url + '/api/v1/courses/' + '{}/quizzes/{}/questions/{}'.format(
            str(init.course_id),
            str(quiz_id),
            str(question_id)),
        params={'access_token': init.access_token},
        data={'question[points_possible]': points})


def get_quiz_questions(quiz_id):
    quiz_questions = requests.get(
        init.base_url + '/api/v1/courses/' + '{}/quizzes/{}/questions'.format(
            str(init.course_id),
            str(quiz_id)),
        params={'access_token': init.access_token, 'per_page': 100})
    return quiz_questions.json()


def get_quiz_group(quiz_id, group_id):
    quiz_group = requests.get(
        init.base_url + '/api/v1/courses/' + '{}/quizzes/{}/groups/{}'.format(
            str(init.course_id),
            str(quiz_id),
            str(group_id)),
        params={'access_token': init.access_token})
    return quiz_group.json()


def delete_quiz_group(quiz_id, group_id):
    quizzes = requests.delete(
        init.base_url + '/api/v1/courses/' + '{}/quizzes/{}/groups/{}'.format(
            str(init.course_id),
            str(quiz_id),
            str(group_id)),
        params={'access_token': init.access_token})


def fix_question_order(quiz_id, payload):
    fixed_question = requests.post(
        init.base_url + '/api/v1/courses/' + '{}/quizzes/{}/reorder'.format(
            str(init.course_id),
            str(quiz_id)),
        params={'access_token': init.access_token},
        json={'order': payload})


def get_full_topic(topic_id):
    full_topic = requests.get(
        init.base_url + '/api/v1/courses/{}/discussion_topics/{}/view'.format(
            str(init.course_id), str(topic_id)),
        params={'access_token': init.access_token})
    return full_topic.json()

def get_all_discussions():
    page_set = []
    # initial request
    buffer100 = requests.get(
        init.base_url + "/api/v1/courses/{}/discussion_topics".format(str(init.course_id)),
        params={'access_token': init.access_token, 'per_page': 100})
    raw = buffer100.json()
    for page in raw:
        page_set.append(page)
    # return pages.json()
    while buffer100.links['current']['url'] != buffer100.links['last']['url']:
        buffer100 = requests.get(
            buffer100.links['next']['url'],
            params={'access_token': init.access_token, 'per_page': 100})
        raw = buffer100.json()
        for page in raw:
            page_set.append(page)
    return page_set

def create_annoucement(announcement_title, announcement_msg):
    annoucement = requests.post(
        init.base_url + '/api/v1/courses/' + "{}/discussion_topics".format(init.course_id),
        params={'access_token': init.access_token,
        'title': announcement_title,
        'message': announcement_msg,
        		'is_announcement': True})

def update_module_item_name(module_ID, item_ID, new_name):
    new_name = requests.put(
        init.base_url + '/api/v1/courses/' + '{}/modules/{}/items/{}'.format(
            str(init.course_id),
            str(module_ID),
            str(item_ID)),
        params={'access_token': init.access_token},
        data={'module_item[title]': new_name})
    return new_name.json()

def get_all_events(quiz_id,submission_id):
    page_set = []
    # initial request
    buffer100 = requests.get(
        init.base_url + "/api/v1/courses/{}/quizzes/{}/submissions/{}/events".format(str(init.course_id),str(quiz_id),str(submission_id)),
        params={'access_token': init.access_token, 'per_page': 100})
    raw = buffer100.json()['quiz_submission_events']
    for page in raw:
        page_set.append(page)
    # return pages.json()
    while buffer100.links['current']['url'] != buffer100.links['last']['url']:
        buffer100 = requests.get(
            buffer100.links['next']['url'],
            params={'access_token': init.access_token, 'per_page': 100})
        raw = buffer100.json()['quiz_submission_events']
        for page in raw:
            page_set.append(page)
    return page_set

def delete_course(course_id):
    deleted_course = requests.delete(
        init.base_url + '/api/v1/courses/' + "{}".format(course_id),
        params={'access_token': init.access_token,
        'event': 'delete'})