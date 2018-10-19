# Course Cleanup Program

## Introduction

The purpose of this program is to clean up courses that have been exported from Blackboard Learn and imported into Canvas. This program can help save time by automating the process of making changes in bulk rather than manually.

### Features of this program include the ability to:

-   Reset courses without changing the course ID

-   Delete unnecessary announcements, assignments, and assignment groups that
    were migrated over from Blackboard Learn.

-   Revert pages to their original state.

-   Convert all HTML files to Canvas pages and fix all broken links that are
    associated to the course. Note: This will not fix any external links.

-   Modifies all external URLs under Modules to load in new tabs

-   Allows module items to be moved in bulk across different modules

-   Publishes all content under Modules

-   Deletes the first text header under each module if it is the first item in
    the module and it has the same title has the module

-   Corrects the Course Name and Course Code of the course

-   Fixes the indentation of the module items

-   Moves all single questions outside of single question quiz groups

-   Removes Page Title Numbering that occurs with identical page names

### Limitations:

-   Supported for PC only.

-   Exporting and importing for Blackboard and Canvas must be done manually.

## Requirements

This program requires one file and two pieces of information:

-   An exported course package file from Blackboard Learn that will be used to
    import to Canvas

-   An “Access Token” to identify a specific user

-   The course ID to identify a specific course

## Creating an Export Package from Blackboard

1.  Access Blackboard and export a course as a Common Cartridge File.
2. Login to Blackboard, then click on the course you want to clean up

3. On the left-hand side menu, click “**Package and Utilities**” to expand
        for more option and then choose “**Export/Archive Course**”.

4. On the top right corner of the page, click “**Export Common Cartridge Package**”

5.  Under the header **Select Common Cartridge Version**, choose “**Export as
    Common Cartridge 1.1**” or “**Export as Common Cartridge 1.2**”

6.  Under the header **Select Content Area**, choose “**All Content Area (as
    Folders)**”

7. Press Submit.

8.  After pressing submit, you will be redirected back to the previous page. You
    will receive an email when the course is ready to be downloaded. Refresh the
    page to see the Common Cartridge File link of your course. Click the Common
    Cartridge File link to download it.


## Import the exported package into Canvas

1. Login to Canvas (*https://canvas.ubc.ca/*) and access your course blank shell.

2. On the left-hand side of the course menu, click “**Settings**”

3.  On the right-hand menu, choose ”**Import Course Content**”

4.  For **Content Type**, in the drop-down menu, select “**Common Cartridge 1.x
    Package**”

5.  For **Source**, click **Choose File** and select the Common Cartridge File
    that was exported from Blackboard Learn.

6.  For **Content**, select “**All content**”


7. Click “**Import”**

1.  The file will begin to import into Canvas.

>   If the course fails to import, please revisit the steps above and try again. Also, if you don’t have a blank shell, it’s recommended that you create one.

## How to get an Access Token

1. Login to Canvas and click on the **Account** icon located on the left-hand menu.

2. Click on Settings


3. Scroll down to the section **Approved Integrations**, click on the button
“**+New Access Token**”

4.  In the field labelled **Purpose**, specify the reasoning for this Access
    Token. The expiration date can be left blank. Next, click “**Generate
    Token**”.


5.  Your Access Token will appear in the section labelled **Token**. Copy this
    long string of text into your clipboard or save it in a text file.


## How to get a course ID

1.  Log into Canvas and go to your course blank shell

2.  In the URL, the last four digits at the end of the URL is your course ID.

## Running the Program
3. Run the file named “course_cleanup.exe” to start the program.

## Logging in

1.  After opening “course_cleanup.exe”, the console should appear immediately.
    However, there may be a short waiting period for the user interface to
    appear on your screen.


2.  After, a pop-up window will appear prompting you to enter your credentials:
    **Course ID** and **Access Token**.

3.  Input the **Course ID** of your course and the **Access Token** tied to your
    account.

4.  Check-off “**Save Access Token**” if you do not wish to always enter your
    Access Token during the login process.

5.  Click “**Ok**” when you are done.

## Navigating the User Interface

By entering your credentials correctly, the program will begin to load the **Course Cleanup Tools** window.

>   **NOTE:** If you enter your credentials incorrectly, the program will display an error message that says, “Course ID or Access Token is incorrect”.


In this window, you will see fourteen (or more) buttons, each with a specific function:

### Forget Access Token

If you checked off the Save Access Token button while entering your credentials, the program will save a file that holds your Access Token in the same directory of the program. Click on this button to delete the file.

### Delete All Content

By running this function, the course will revert back to a course shell. Primarily, this will delete **ALL** the content within the course without changing the course ID.

### Delete Excess Content

This will remove assignments and assignment groups specifically named as: “Program”, “Majors”, “Year Level”, “Faculty”, “Minors”, “Term”, “Linked
Section”, “Discussion”, “Lab”, “Program Year”, “Section”, “Status”, and “Tutorial”.

It will also delete all announcements.

### Revert Pages to First Version

This will revert all pages to their initial unedited version. This means that changes made to all pages will be reset.

### Convert HTML Files to Pages

This will convert all HTML Files to Canvas Pages in the course. It will also fix all page-to-page links and page-to-file/image links associated with these converted HTMLs.

### Try Another Course

This will prompt the user to enter another course they wish to have cleaned-up.

### External Links to New Tabs

This will modify all external URL items under modules to load in new tabs.

### Mass Move Items to Module

This function allows the user to move any selected group of module items to the top of any module.

### Publish All

This will publish all the items and modules under Modules in the course.

### Delete First Text Header

If there exists a Text Header which has the same title as its module and sits at the top of its module, it will be deleted.

### Correct Course Name and Course Code
This function will correct the Course Name and Course Code of the course if it is missing the professor’s last name or the year it was offered.

### Push Indents to Left

This function will decrease the indents of all module items until one of the items hits the leftmost margin of the module.

### Fix Single Question Quiz Groups
This function will extract single questions outside their question group if it is the only question in its group. The extracted question will take on
the point value of the question group it left. The empty question group will be deleted afterwards.

### Remove Page Title Numbering

This function will remove the numbering that occurs when page titles have the same name (for example, test and test-2)

## Using the Program

If you click on any one of the buttons, the message box at the bottom of the window will change. A spinning icon will appear and the console will begin
printing out messages to indicate that the program is successfully running.


Once the program runs successfully, the message box will say “**done**”. At this time, you can call another function by clicking on another button.

>  **NOTE**: If you need to force stop the program, exit the user interface and console by closing both windows.

## Use Cases

### Forget Access Token

If another person wants to enter their credentials and run the program under their account, forgetting the Access Token will delete the file holding the
old Access Token and prompt a user for a new Access Token upon the next
login.

>   **NOTE**: If you regenerate your Access Token on Canvas without forgetting
>   the Access Token, the program will try to read your old Access Token file
>   upon your next login and it will encounter an error. To fix this issue, you
>   will need to delete the file called “deets” located in the same directory as
>   the program.

### Delete All Content

If you need to reset a course without changing the course ID, please choose this option.

### Revert Pages to First Version

This reverts all pages to its initial version before any edits were made. This is useful after converting HTMLs to pages because users will have a snapshot of their course after the conversion.

### Convert HTML to Pages
All HTMLs exported from Blackboard Learn and imported into Canvas will show up as attachments. This function will convert all HTMLs from ‘Attachment’ type to ‘Page’ type. It will also fix all page-to-page links and page-to-file/image links associated with these HTMLs. In other words, if an HTML is linked to another HTML, file, or image, a converted HTML page will now link to another converted HTML page, file, or image.

### Delete Excess Content
After exporting from Blackboard Learn and importing into Canvas, some excess assignments, assignment groups, and announcements may also be transferred
over. These assignments and assignments groups are specifically named
“Program”, “Majors”, “Year Level”, “Faculty”, “Minors”, “Term”, “Linked
Section”, “Discussion”, “Lab”, “Program Year”, “Section”, “Status”, and
“Tutorial”. Empty announcements may also be migrated over. This function
will remove all these elements.

### Try Another Course

Cleaning up multiple courses may be a hassle if the program constantly needs
to be closed and reopened every time you want to switch courses. This will
allow you to switch courses within the program.

### External Links to New Tabs

Sometimes external links are not rendered because they are inaccessible from
Canvas’ servers. Therefore, it is a better idea to always load external
links in new tabs. Running this function will modify all external URLs under
Modules to load in new tabs.

### Mass Move Items to Module
Since Canvas can only nest items two levels deep under Modules (the actual
module and the module items that sit within it), content imported from
Connect all be thrown into a single module with indents acting as deeper
levels of nesting. This can look very overwhelming for the end-user. It is
better to separate deeper nested items into separate modules. After creating
these separate modules, it may be tedious to move items into them by
dragging and dropping one-by-one. This function allows users to move items
all at once to a specific module of their choice.

### Publish All

This function will publish all modules and items under Modules in the
    course. Canvas has trouble identifying hidden and visible links in Connect
    and makes its own judgment call to publish or not publish certain items
    after importing. Publishing all items makes everything consistent, so the
    instructor of the course can unpublish any undesired items after the
    clean-up.

### Delete First Text Header

Since folders/modules in Connect can hold metadata, Canvas will sometimes
    create a page or a text header that sits as the first item in a module and
    has the same title as that module. Indeed, if it is a page, it may contain
    some important information about the module so deleting it would be
    problematic. However, if it is a text header, it will not hold any
    additional information about the module, so deleting it would be ideal.

### Correct Course Name and Course Code

Course names that follow the structure: [MG] [Name of Course] [Year Offered]
    – [Professor’s last name], may have some missing information; usually the
    year offered or professor’s last name. This function parses the course name
    and checks if the year offered or professor’s last is included. If not, it
    will prompt the user for the information. It will then update the Course
    name and Course Code of the course automatically.

### Push indents to left

After moving around module items in the course, the indentation of the
    module items may not consistently sit on the left margin of the module. This
    function will decrease the indentation of all items in a module until an
    item hits the leftmost margin of the module. This will retain the overall
    structure of the module and reduces the number of clicks needed to decrease
    the indentation of every module item manually.

### Fix Single Question Quiz Groups

Exporting quizzes from Connect and importing them into Canvas has always
    yielded some issues. One of these issues include question groups in quizzes
    that only hold a single question in them. This moves all single questions in
    a single question group outside the question group and then deletes the
    empty question group afterwards. The extracted question will also take the
    point value specified in its question group. This is useful because it
    cleans up the quiz questions and maintains the order of the questions when it was imported.

### REMOVE PAGE TITLE NUMBERING

   Canvas does not allow identical page titles. If two different pages have
    identical page titles, Canvas will add numbering at the end of one of the
    page titles to distinguish it from the other. This function will replace the
    numbering with spaces, so visually, page title names will look identical.
    This is useful because running HTML to Pages sometimes converts html files
    that have the same name as existing Canvas Pages. Running this function
    effectively allows for page titles to visually have the same name.

## Exampling: Running the Program for an HTML-heavy course

1.  Export a course from Blackboard Learn as a Common Cartridge File and import
    it into Canvas

2.  Run the program and input the correct Course ID and Access Token

3.  Run HTML to Pages

4.  Run External Links to New Tabs

5.  Run Fix Single Question Quiz Groups

6.  If needed, use Mass Move Items to Module

7.  If needed, run Push Indents to Left

8.  If needed, run Remove Page Title Numbering

9.  Run Delete First Text Header

10. Run Publish All

11. Run Delete Excess Content
