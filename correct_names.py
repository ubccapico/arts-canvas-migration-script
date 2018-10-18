import init
import api_calls as api
import pprint
import re
import tkinter as tk
from tkinter import *
from tkinter import simpledialog


def has_date(array):
    for elem in array:
        check = re.match(r'[\d]{4}[A-z]{1}[\d]{1}', elem)
        if check:
            return True


def has_last_name(course_name_param):
    pattern = re.compile(r"(?:-[ ]*[a-zA-Z']+)+$")
    if pattern.search(course_name_param):
        return True


def name_to_code(name):
    course_name_array = name.split(' ')[:4]
    course_name_array[1:3] = [''.join(course_name_array[1:3])]
    course_name_array[0] = course_name_array[0].replace("[", "")
    course_name_array[0] = course_name_array[0].replace("]", "")
    parsed_course_array = '.'.join(course_name_array)
    return parsed_course_array


def correct_names(self):
    flag = False
    course_info = api.get_course()
    course_name = course_info['name']
    new_course_code = name_to_code(course_name)
    # course_code = course_info['course_code']

    if not has_last_name(course_name):
        try:
            last_name = simpledialog.askstring("Enter Last Name", "What is professor's last name?",
                                parent=self.master)
            course_name = course_name + ' - ' + last_name.upper()
            flag = True
        except AttributeError:
            pass

    course_name_array = re.findall(r"[[*(*&*,*.*\w.*,*'*\]\{*})*]+", course_name)
    if not has_date(course_name_array):
        try:
            date = simpledialog.askstring("Enter Course Name", "When is the course offered?",
                                    parent=self.master)
            course_name_array.insert(len(course_name_array)-1, date.upper())
            print(course_name_array)
            course_name_array[len(course_name_array)-1] = "- " + course_name_array[len(course_name_array)-1]
            course_name = ' '.join(course_name_array)
            flag = True
        except AttributeError:
            pass


    new_course_name = course_name



    if flag:
        api.update_course_name(new_course_name)
        api.update_course_code(new_course_code)
        print('The new course name is: ' + new_course_name)
        print('The new course code is: ' + new_course_code)
