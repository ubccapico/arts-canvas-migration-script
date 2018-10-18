#!/usr/bin/env python

import os
import time
import threading
import traceback
import pprint

from tkinter import *
from tkinter import messagebox, simpledialog

import init
import api_calls as api
import delete_course as delete_course_module
import delete_excess as delete_excess_module
import files_to_pages as ftp
import restore_all_pages as rap
import external_links_new_tab as elnt
import mass_move as mm
import publish_all as pa
import same_module_and_first_text_header as smafth
import correct_names as cn
import push_indents_to_left as pitl
import fix_question_groups as fqg
import remove_page_title_numbering as rptn
import remove_module_item_file_extensions as rmife
import delete_duplicate_name_and_type_module_item as ddnatmi


faculty = ''
course_name = ''
short_course_name = ''
course_code = ''



class Example(Frame):
    def __init__(self, root):

        Frame.__init__(self, root)
        root.geometry('380x600')
        self.canvas = Canvas(root, borderwidth=0, background="#ffffff")
        self.frame = Frame(self.canvas, background="#ffffff")
        self.vsb = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4, 4), window=self.frame, anchor="nw", tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)
        self.populate()

    def populate(self):

        f1 = Frame(self.frame)

        # Create a Tkinter variable
        self.tkvar = StringVar(self.frame)
 
        # Dictionary with options
        all_modules = mm.get_all_modules()
        self.data = dict()
        for module in all_modules:
            self.data[str(module['name'])] = module['id']

        if len(all_modules) == 0:
            print("Mass Move Items to Module cannot be run because there are no modules in this course")
            return

        self.tkvar.set(next(iter(self.data)))
 
        popupMenu = OptionMenu(f1, self.tkvar, *self.data.keys())
        Label(f1, text="Select a Module:").grid(row = 0, column = 0,sticky='W')
        Button(f1, text="Create a new module",command=self.create_new_module).grid(row = 0, column = 2, sticky='E')
        popupMenu.grid(row = 0, column =1,sticky='W')

        f1.grid(row = 0, column =0,sticky='NEWS')

        self.global_state = BooleanVar()
        select_all = Checkbutton(self.frame, text="select/deselect all",
                            variable=self.global_state,
                            command=self.select_clear_states)
        select_all.grid(row=1, column=0, padx=0, pady=1, sticky='W')

        self.itemArray = mm.get_all_items()
        self.states = []
        self.start = 0
        self.chkbuttons = []
        self.counter = 0

        for index, item in enumerate(self.itemArray):
            var = BooleanVar()
            var_string = StringVar()
            if item['type'] is 'item':
                indent = item['indent']*20
                paddy_y = 1
                cb = Checkbutton(self.frame, text=str(item['title']), variable=var)
                var_string.set('0')

            if item['type'] is 'module':
                paddy_y = 20
                indent = 0
                cb = Label(self.frame, text=item['name'], font=("Helvetica", 12, 'bold'))

            cb.grid(row=index+2, column=0, padx=indent, pady=(paddy_y, 1), sticky='W')

            self.states.append(var)
            cb.bind("<Button-1>", self.selectstart)
            cb.bind("<Shift-Button-1>", self.selectrange)
            self.chkbuttons.append(cb)

        Button(self.frame, text='Mass Move Items', command=self.var_states).grid(row=len(self.states)+2, sticky='W', pady=4)
        self.frame.loading = Label(
            self.frame,
            text='Please choose items to move...',
            anchor=W)
        self.frame.loading.grid(row=len(self.states)+3, columnspan=2, sticky='w')
        self.update_boolean_state = BooleanVar()
        self.frame.update_boolean = Checkbutton(self.frame, text="do not update list after mass moving",
                            variable=self.update_boolean_state)
        self.frame.update_boolean.grid(row=len(self.states)+4, columnspan=2, sticky='w')

    def create_new_module(self):
        module_name = simpledialog.askstring("Enter Module Name", "What is the name of the new module?",
                            parent=self.master)
        if module_name is not None:
            thread = threading.Thread(target=api.create_new_module, args=(module_name,))

            thread.start()
            cycle = ['/', '-', '\\']
            eli_count = 0
            while thread.is_alive():
                self.update()
                eli_count = (eli_count + 1) % 3
                self.frame.loading['text'] = 'The new module "' + module_name + '" is currently being created...' + str(cycle[eli_count])
                self.master.update()
                time.sleep(0.1)
            thread.join()

            if self.update_boolean_state.get() is False:
                self.frame.loading['text'] = 'Please wait, updating list after adding the new module "'+ module_name +'"...'
                self.master.update()
                for widget in self.frame.winfo_children():
                    widget.destroy()
                self.populate()
            else:
                self.frame.loading['text'] = 'Done creating "'+ module_name +'"!'


    def var_states(self):
        class TrueItem(object):
            def __init__(self, item_id, item_module_id, item_title):
                self.item_id = item_id
                self.item_module_id = item_module_id
                self.item_title = item_title

        Trues = []
        dest = self.data[self.tkvar.get()]
        for index, boolean in enumerate(self.states):
            if (boolean.get() is True):
                Trues.append(TrueItem(self.itemArray[index]['id'],self.itemArray[index]['module_id'],self.itemArray[index]['title']))
        thread = threading.Thread(target=mm.mass_move, args=(dest, Trues,))

        thread.start()
        cycle = ['/', '-', '\\']
        eli_count = 0
        while thread.is_alive():
            self.update()
            eli_count = (eli_count + 1) % 3
            self.frame.loading['text'] = 'The items are currently being moved... ' + str(cycle[eli_count])
            self.master.update()
            time.sleep(0.1)
        thread.join()
        if self.update_boolean_state.get() is False:
            self.frame.loading['text'] = 'Please wait, updating list...'
            self.master.update()
            for widget in self.frame.winfo_children():
                widget.destroy()
            self.populate()
        else:
            self.frame.loading['text'] = 'All items have been moved successfully!'

    def selectstart(self, event):
        self.start = self.chkbuttons.index(event.widget)

    def selectrange(self, event):
        start = self.start
        end = self.chkbuttons.index(event.widget)
        sl = slice(min(start, end)+1, max(start, end))
        for cb in self.chkbuttons[sl]:
            try:
                cb.toggle()
            except AttributeError:
                pass
        self.start = end


    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/60)), "units")

    def select_clear_states(self):
        # get global checkbox
        state = self.global_state.get()

        # set all "small" checkboxes
        for x in self.states:
            x.set(state)

class PopUp(Toplevel):

    def __init__(self):
        Toplevel.__init__(self)
        Example(self).pack(side="top", fill="both", expand=True)


def popup():

    win = PopUp()

def center(top_level):
    top_level.withdraw()
    top_level.update_idletasks()
    x = (top_level.winfo_screenwidth() - top_level.winfo_reqwidth()) / 2
    y = (top_level.winfo_screenheight() - top_level.winfo_reqheight()) / 2
    top_level.geometry("+%d+%d" % (x, y))
    top_level.deiconify()


def thread_message(self, messageParam, function):
    thread = threading.Thread(target=function)
    thread.start()
    cycle = ['/', '-', '\\']
    eli_count = 0
    while thread.is_alive():
        eli_count = (eli_count + 1) % 3
        self.frame.status['text'] = messageParam + ' ' + str(cycle[eli_count])
        self.master.update()
        time.sleep(0.1)
    thread.join()


class EnterCredentials:
    def __init__(self, master):
        # master refers to the window
        self.master = master

        # setting master title
        master.title('Enter Credentials')

        # centering master
        center(master)
      #  master.geometry("275x95")

        # put frame into master and configure grid
        self.frame = Frame(self.master)
        self.frame.pack(fill="both", expand=True)
        self.frame.grid_rowconfigure(4, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)

        # Course ID Label
        self.frame.course_id = Label(self.frame, text="Course ID: ")
        self.frame.course_id.grid(row=0, sticky=E)

        # Course ID Entry
        self.frame.course_id_entry = Entry(self.frame)
        self.frame.course_id_entry.grid(row=0, column=1, sticky='news')

        # Base URL Label
        self.frame.base_url = Label(self.frame, text="Base URL: ")
        self.frame.base_url.grid(row=1, sticky=E)

        # Base URL Entry
        self.frame.base_url_entry = Entry(self.frame)
        self.frame.base_url_entry.grid(row=1, column=1, sticky='news')

        self.frame.access_token = Label(self.frame, text="Access Token: ")
        self.frame.access_token.grid(row=2, sticky=E)

        self.frame.access_token_entry = Entry(self.frame)
        self.frame.access_token_entry.grid(row=2, column=1, sticky='news')

        self.master.bind('<Return>', self.new_window)
        self.master.bind('<Escape>', self.close_windows)

        # Ok Button
        self.frame.login_button_ok = Button(
            self.frame, text="Ok", command=self.new_window)
        self.frame.login_button_ok.grid(row=4, column=0, sticky='news')

        # Cancel Button
        self.frame.login_button_cancel = Button(
            self.frame, text="Cancel", command=self.close_windows)
        self.frame.login_button_cancel.grid(row=4, column=1, sticky='news')

    def close_windows(self, event=None):
        self.master.destroy()

    def new_window(self, event=None):
        try:
            # record course_idas
            init.course_id = self.frame.course_id_entry.get()
            init.base_url = self.frame.base_url_entry.get()
            init.access_token = self.frame.access_token_entry.get()


            global short_course_name
            short_course_name = self.frame.course_id_entry.get()
            global course_name
            course_name = api.get_course()['name']
            global course_code
            course_code = api.get_course()['course_code']

            # if everything comes back fine, destroy this EnterCredentials
            # window and create CourseCleanupOptions window
            self.master.destroy()
            self.master = Tk()
            self.app = CourseCleanupOptions(self.master)
            self.master.mainloop()
        except Exception as e:
            #traceback.print_exc()
            print('The Course ID, Access Token, or base URL is incorrect.\nIf any problem still persists, restart the program, delete the deets file, and try again.')
            messagebox.showinfo(
                "Error",
                "The Course ID, Access Token, or base URL is incorrect.",
                icon="warning")


class CourseCleanupOptions:

    def __init__(self, master):
        # master refers to the window
        self.master = master

        # setting master title
        master.title('Course Cleanup Tools')

        # centering master
        center(master)

        # frame sits within master
        self.frame = Frame(self.master)
        self.frame.pack(fill="both", expand=True)
        self.frame.grid_rowconfigure(3, weight=1)
        self.frame.grid_rowconfigure(4, weight=1)
        self.frame.grid_rowconfigure(5, weight=1)
        self.frame.grid_rowconfigure(6, weight=1)
        self.frame.grid_rowconfigure(7, weight=1)
        self.frame.grid_rowconfigure(8, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_columnconfigure(2, weight=1)

        # Course ID Label
        self.frame.course_id = Label(self.frame, text="Course ID:")
        self.frame.course_id.grid(row=0, sticky=E)

        # Course ID Info Label
        self.frame.course_id_info = Label(self.frame, text=short_course_name)
        self.frame.course_id_info.grid(
            row=0, column=1, columnspan=2, sticky='w')

        # Course Name Label
        self.frame.course_name = Label(self.frame, text="Course Name:")
        self.frame.course_name.grid(row=1, sticky=E)

        # Course Name Info Label
        self.frame.course_name_info = Label(self.frame, text=course_name)
        self.frame.course_name_info.grid(
            row=1, column=1, columnspan=2, sticky='w')

        # Course Code Label
        self.frame.course_code = Label(self.frame, text="Course Code:")
        self.frame.course_code.grid(row=2, sticky=E)

        # Course Code Info Label
        self.frame.course_code_info = Label(self.frame, text=course_code)
        self.frame.course_code_info.grid(row=2, column=1, columnspan=2, sticky='w')

        # Forget Token Button
        self.frame.forget_token = Button(
            self.frame, text="Forget Access Token", command=self.forget_token)
        self.frame.forget_token.grid(row=3, column=0, sticky='news')

        # Delete Course Button
        self.frame.delete_course = Button(
            self.frame,
            text="Delete All Content",
            command=self.delete_course_function)
        self.frame.delete_course.grid(row=3, column=1, sticky='news')

        # Revert to First Version Button
        self.frame.revert_first_version = Button(
            self.frame,
            text="Revert Pages to First Version",
            command=self.revert_first_version_function)
        self.frame.revert_first_version.grid(row=3, column=2, sticky='news')

        # File to Pages Button
        self.frame.file_to_pages = Button(
            self.frame,
            text="Convert HTML Files to Pages",
            command=self.file_to_pages_function)
        self.frame.file_to_pages.grid(row=4, column=0, sticky='news')

        # Delete Excess Content Button
        self.frame.delete_excess_content = Button(
            self.frame,
            text="Delete Excess Content", command=self.delete_excess)
        self.frame.delete_excess_content.grid(row=4, column=1, sticky='news')

        # New Course Button
        self.frame.another_course = Button(
            self.frame,
            text="Try Another Course",
            command=self.another_course)
        self.frame.another_course.grid(row=4, column=2, sticky='news')

        # External Links to new Tab Button
        self.frame.external_links_new_tabs = Button(
            self.frame,
            text="External Links to New Tabs",
            command=self.external_links_new_tabs)
        self.frame.external_links_new_tabs.grid(row=5, column=0, sticky='news')

        # Mass move Button
        self.frame.mass_move = Button(
            self.frame,
            text="Mass Move Items to Module",
            command=self.mass_move)
        self.frame.mass_move.grid(row=5, column=1, sticky='news')

        # Publish All Button
        self.frame.publish_all = Button(
            self.frame,
            text="Publish All",
            command=self.publish_all)
        self.frame.publish_all.grid(row=5, column=2, sticky='news')

        # Delete Same Text Header and Module Button
        self.frame.same_text_header = Button(
            self.frame,
            text="Delete First Text Header or Page",
            command=self.same_text_header)
        self.frame.same_text_header.grid(row=6, column=0, sticky='news')

        # Correct Names Button
        self.frame.correct_names = Button(
            self.frame,
            text="Correct Course Name and Course Code",
            command=self.correct_names)
        self.frame.correct_names.grid(row=6, column=1, sticky='news')

        # Push Indents to Left Button
        self.frame.push_indents_to_left = Button(
            self.frame,
            text="Push Indents to Left",
            command=self.push_indents_to_left)
        self.frame.push_indents_to_left.grid(row=6, column=2, sticky='news')

        # Single Question Quiz Groups Button
        self.frame.fix_question_groups = Button(
            self.frame,
            text="Fix Single Question Quiz Groups",
            command=self.fix_question_groups)
        self.frame.fix_question_groups.grid(row=7, column=0, sticky='news')

        # Remove Page Title Numbering Button
        self.frame.remove_page_title_numbering = Button(
            self.frame,
            text="Remove Page Title Numbering",
            command=self.remove_page_title_numbering)
        self.frame.remove_page_title_numbering.grid(row=7, column=1, sticky='news')

        # Remove Module Item File Extensions Button
        self.frame.remove_module_item_file_extensions = Button(
            self.frame,
            text="Remove Module Item File Extensions",
            command=self.remove_module_item_file_extensions)
        self.frame.remove_module_item_file_extensions.grid(row=7, column=2, sticky='news')

        # Delete Duplicate name and type module item
        self.frame.delete_dup_name_and_type = Button(
            self.frame,
            text="Delete duplicate name and type module items",
            command=self.delete_dup_name_and_type)
        self.frame.delete_dup_name_and_type.grid(row=8, column=0, sticky='news')

        # Help Button
        self.frame.help = Button(
            self.frame,
            text="Help",
            relief=GROOVE,
            command=self.help_box)
        self.frame.help.grid(row=0, column=2, sticky='ne')

        # Status Label
        self.frame.status = Label(
            self.frame,
            text='Choose an option...',
            bd=1,
            relief=SUNKEN,
            anchor=W)
        self.frame.status.grid(row=9, columnspan=3, sticky='news')

    def help_box(self):
        messagebox.showinfo(
            "Help",
            "Forget Access Token: Removes file that stores the access token."
            "\n\nDelete All Content: Removes all Course Content without"
            " changing the Course ID.\n\nRevert to First Version: "
            "Reverts all pages to initial version (no edits made)"
            "\n\nConvert HTML files to Pages: Converts all HTML files to "
            "Pages (from type 'Attachment' to type 'Page'), fixes page to "
            "page links, and fixes page to file/image links \n\nDelete "
            "Excess Content: Removes excess annoucements, assignment groups, "
            "and assignments that may have migrated over when importing from "
            "Connect.\n\nTry Another Course: Switch to another course "
            "that you wish to clean up.\n\nExternal Links to New Tabs: "
            "Modifies all external URLs under modules to load in new tabs."
            "\n\nMass Move Items to Module: Allows the user to move module"
            " items in bulk to the top of any specific module.\n\n"
            "Publish All: Publishes all modules and module items in the course."
            "\n\nDelete First Text Header: Deletes the text header if it"
            " is the first item in its module and has the same title as "
            "its module.\n\nCorrect Course Name and Course Code: "
            "Corrects the course name and course code if it is in the form:"
            " [MG] [Name of Course] [Year Offered] - [Professor Last name]"
            "\n\nPush Indents to Left: Decreases the indents of all items" 
            " in a module until one item hits the leftmost margin of the "
            "module.\n\nFix Single Question Quiz Groups: Extracts single "
            "questions outside of single question groups.\n\nRemove Page"
            " Title Numbering: Removes the numbering at the end of pages "
            "that occur when pages have identical page titles to each other.")

    def forget_token(self):
        self.frame.status['text'] = 'Forgetting Access Token...'
        self.frame.update_idletasks()
        time.sleep(1)
        if os.path.isfile('deets'):
            os.remove('deets')

        self.frame.status['text'] = 'Done Forgetting Access Token!'
        self.frame.update_idletasks()

    def delete_course_function(self):
        result = messagebox.askquestion(
            "Delete All Content",
            "Are you sure you want to delete ALL course content?",
            icon='warning')
        if result == 'yes':
            thread_message(
                self,
                'Deleting All Course Content...',
                delete_course_module.delete_course)
            self.frame.status['text'] = 'Done Deleting All Course Content!'
            self.frame.update_idletasks()

    def revert_first_version_function(self):
        thread_message(
            self,
            "Reverting to the First Version...",
            rap.master_rap)
        self.frame.status['text'] = 'Done reverting to the First Version!'
        self.frame.update_idletasks()

    def file_to_pages_function(self):
        thread_message(self, "Running File to Pages...", ftp.master_ftp)
        self.frame.status['text'] = 'Done converting Files to Pages!'
        self.frame.update_idletasks()

    def delete_excess(self):
        result = messagebox.askquestion(
            "Delete Excess Material",
            "Are you sure you want to delete annoucements, "
            "empty assignment groups, unnecessary "
            "assignments, and empty folders in this course?",
            icon='warning')
        if result == 'yes':
            thread_message(
                self,
                'Deleting Excess Material...',
                delete_excess_module.master_delete_excess)
            self.frame.status['text'] = 'Done deleting Excess Material!'
            self.frame.update_idletasks()

    def another_course(self):
        try:
            original_course_id = init.course_id
            var = simpledialog.askstring("Try Another Course", "Course ID:")
            if var is None:
                raise ValueError('Cancelled or Exited')
            # record course_id
            init.course_id = var
            global short_course_name
            short_course_name = var
            global course_name
            course_name = api.get_course()['name']
            global course_code
            course_code = api.get_course()['course_code']

            # if everything comes back fine, destroy this EnterCredentials
            # window and create CourseCleanupOptions window
            self.master.destroy()
            self.master = Tk()
            self.app = CourseCleanupOptions(self.master)
            self.master.mainloop()
        except Exception as e:
            init.course_id = original_course_id
            if str(e) == 'Cancelled or Exited':
                pass
            else:
                messagebox.showinfo(
                    "Error", "Course ID is incorrect.", icon="warning")

    def external_links_new_tabs(self):
        thread_message(
            self,
            "Running External Links to New Tabs...",
            elnt.external_links_new_tab)
        self.frame.status['text'] = 'Done running External Links to New Tabs!'
        self.frame.update_idletasks()

    def mass_move(self):
        PopUp()
        # thread_message(
        #     self,
        #     "Running Mass Move Items to Module...",
        #     mm.mass_move)
        # self.frame.status['text'] = 'Done running Mass Move Items to Module!'
        self.frame.update_idletasks()

    def publish_all(self):
        thread_message(
             self,
             "Running Publish All...",
             pa.publish_all)
        self.frame.status['text'] = 'Done Publishing All!'
        self.frame.update_idletasks()

    def same_text_header(self):
        thread_message(
             self,
             "Running Deleting Same Text Header or Page to Module...",
             smafth.same_module_text_header)
        self.frame.status['text'] = 'Done deleting same Text Header or Page to Module!'
        self.frame.update_idletasks()

    def correct_names(self):
        thread_message(
             self,
             "Running Correct Course Name and Course Code...",
             cn.correct_names(self))
        self.frame.status['text'] = 'Done running Correct Course Name and Course Code!'
        course_info = api.get_course()
        global course_name
        course_name = course_info['name']
        self.frame.course_name_info.configure(text=course_name)
        global course_code
        course_code = course_info['course_code']
        self.frame.course_code_info.configure(text=course_code)
        self.frame.update_idletasks()

    def push_indents_to_left(self):
        thread_message(
             self,
             "Running Pushing Indents to Left...",
             pitl.push_indents_to_left)
        self.frame.status['text'] = 'Done pushing indents to left!'
        self.frame.update_idletasks()

    def fix_question_groups(self):
        thread_message(
             self,
             "Fixing Single Question Quiz Groups...",
             fqg.fix_question_groups)
        self.frame.status['text'] = 'Done Fixing Single Question Quiz Groups!'
        self.frame.update_idletasks()

    def remove_page_title_numbering(self):
        thread_message(
             self,
             "Removing Page Title Numbering...",
             rptn.remove_page_title_numbering)
        self.frame.status['text'] = 'Done Removing Page Title Numbering!'
        self.frame.update_idletasks()

    def remove_module_item_file_extensions(self):
        thread_message(
             self,
             "Removing File Extensions from Module Items...",
             rmife.remove_file_extension_from_module_items)
        self.frame.status['text'] = 'Done Removing File Extensions from Module Items!'
        self.frame.update_idletasks()

        delete_dup_name_and_type

    def delete_dup_name_and_type(self):
        thread_message(
             self,
             "Deleting Duplicate name and type module items...",
             ddnatmi.delete_dup_name_and_type)
        self.frame.status['text'] = 'Done deleting duplicate name and type module items!'
        self.frame.update_idletasks()

root = Tk()
app = EnterCredentials(root)
root.mainloop()
