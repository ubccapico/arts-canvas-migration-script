>   COURSE CLEANUP PROGRAM

>   INTRODUCTION

>   The purpose of this program is to clean up courses that have been exported
>   from Blackboard Learn and imported into Canvas. This program can help save
>   time by automating the process of making changes in bulk rather than
>   manually.

>   Features of this program include the ability to:

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

>   Limitations:

-   Supported for PC only.

-   Exporting and importing for Blackboard and Canvas must be done manually.

>   REQUIREMENTS

>   This program requires one file and two pieces of information:

-   An exported course package file from Blackboard Learn that will be used to
    import to Canvas

-   An “Access Token” to identify a specific user

-   The course ID to identify a specific course

>   CREATING AN EXPORT PACKAGE FROM CANVAS

1.  Access Blackboard and export a course as a Common Cartridge File.

    ![](media/28b0026a9c4c3e4e802a56a785a89c15.jpg)

    Login to Blackboard, then click on the course you want to clean up

    1.  On the left-hand side menu, click “**Package and Utilities**” to expand
        for more option and then choose “**Export/Archive Course**”

![](media/1cc2c294269a24873da76d3276c3bd62.jpg)

![](media/f01a72b6bacb5aeaec9b647168a259dd.jpg)

On the top right corner of the page, click “**Export Common Cartridge Package**”

1.  Under the header **Select Common Cartridge Version**, choose “**Export as
    Common Cartridge 1.1**” or “**Export as Common Cartridge 1.2**”

2.  Under the header **Select Content Area**, choose “**All Content Area (as
    Folders)**”

![](media/6d5ba56aabdaab9301d9338cb7e6446d.jpg)

Press Submit.

1.  After pressing submit, you will be redirected back to the previous page. You
    will receive an email when the course is ready to be downloaded. Refresh the
    page to see the Common Cartridge File link of your course. Click the Common
    Cartridge File link to download it.

![](media/fb06da08b825268ba6102d1f6debc604.jpg)

1.  Import the exported Common Cartridge File from Blackboard Learn into Canvas:

    1.  Login to Canvas (*https://canvas.ubc.ca/*) and access your course blank
        shell.

>   *Note: If you don’t have a blank shell, it’s recommended that you create
>   one.*

![](media/dece74ff11b7adb00532544111870185.jpg)

On the left-hand side of the course menu, click “**Settings**”

![](media/f2d16cf70afd34f6daa8ac642c2b5c3f.jpg)

On the right-hand menu, choose ”**Import Course Content**”

1.  For **Content Type**, in the drop-down menu, select “**Common Cartridge 1.x
    Package**”

2.  For **Source**, click **Choose File** and select the Common Cartridge File
    that was exported from Blackboard Learn.

3.  For **Content**, select “**All content**”

![](media/4240fe8f3479e3662bac80a04ae0012c.jpg)

Click “**Import”**

1.  The file will begin to import into Canvas.

![](media/6e5ab37d320406b75cdc2feea0b1b91b.jpg)

>   IMPORTANT: If the course fails to import, please revisit the steps above and
>   try again.

>   HOW TO GET AN ACCESS TOKEN

![](media/c0f839a6da2c753ca3e25765ee44db0f.jpg)

Login to Canvas and click on the **Account** icon located on the left-hand menu.

![](media/b58008a8afd7d80467412923adb0159f.jpg)

Click on Settings

![](media/b28cc2f117ef193618cd2bafad5250d8.jpg)

Scroll down to the section **Approved Integrations**, click on the button
“**+New Access Token**”

1.  In the field labelled **Purpose**, specify the reasoning for this Access
    Token. The expiration date can be left blank. Next, click “**Generate
    Token**”.

![](media/f97b24f35fd4fd2bb22ee474850f8217.jpg)

1.  Your Access Token will appear in the section labelled **Token**. Copy this
    long string of text into your clipboard or save it in a text file.

![](media/8f8802327e1d11a450c15e3cb1a83b23.jpg)

>   HOW TO GET A COURSE ID

1.  Log into Canvas and go to your course blank shell

2.  In the URL, the last four digits at the end of the URL is your course ID.

![C:\\Users\\Andre\\Desktop\\hohohoho3.png](media/a19bbe6346b5986266425347c55b3219.png)

>   Run the file named “course_cleanup.exe” to start the program.

>   LOGGING IN

1.  After opening “course_cleanup.exe”, the console should appear immediately.
    However, there may be a short waiting period for the user interface to
    appear on your screen.

![](media/c6a2f6f78ce064997dcc406916a86791.png)

1.  After, a pop-up window will appear prompting you to enter your credentials:
    **Course ID** and

Access Token.
=============

1.  Input the **Course ID** of your course and the **Access Token** tied to your
    account.

2.  Check-off “**Save Access Token**” if you do not wish to always enter your
    Access Token during the login process.

![](media/b66173ae50b506b963d5a657b056a09b.png)

1.  Click “**Ok**” when you are done.

>   NAVIGATING THE USER INTERFACE

1.  By entering your credentials correctly, the program will begin to load the
    **Course Cleanup Tools**

>   window.

>   **NOTE:** If you enter your credentials incorrectly, the program will
>   display an error message that says, “Course ID or Access Token is
>   incorrect”.

![](media/b6c08d5803526c3a598f2aefabafc9da.png)

>   In this window, you will see fourteen buttons, each with a specific
>   function:

![](media/2cb406dad8a0c93fd22724456c400503.png)

Forget Access Token
===================

>   If you checked off the Save Access Token button while entering your
>   credentials, the program will save a file that holds your Access Token in
>   the same directory of the program. Click on this button to delete the file.

Delete All Content
==================

>   By running this function, the course will revert back to a course shell.
>   Primarily, this will delete **ALL** the content within the course without
>   changing the course ID.

Delete Excess Content
=====================

>   This will remove assignments and assignment groups specifically named as:
>   “Program”, “Majors”, “Year Level”, “Faculty”, “Minors”, “Term”, “Linked
>   Section”, “Discussion”, “Lab”, “Program Year”, “Section”, “Status”, and
>   “Tutorial”.

>   It will also delete all announcements.

Revert Pages to First Version
=============================

>   This will revert all pages to their initial unedited version. This means
>   that changes made to all pages will be reset.

Convert HTML Files to Pages
===========================

>   This will convert all HTML Files to Canvas Pages in the course. It will also
>   fix all page-to- page links and page-to-file/image links associated with
>   these converted HTMLs.

Try Another Course
==================

>   This will prompt the user to enter another course they wish to have
>   cleaned-up.

1.  **External Links to New Tabs**

>   This will modify all external URL items under modules to load in new tabs.

1.  **Mass Move Items to Module**

>   This function allows the user to move any selected group of module items to
>   the top of any module.

1.  **Publish All**

>   This will publish all the items and modules under Modules in the course.

1.  **Delete First Text Header**

>   If there exists a Text Header which has the same title as its module and
>   sits at the top of its module, it will be deleted.

1.  **Correct Course Name and Course Code**

>   This function will correct the Course Name and Course Code of the course if
>   it is missing the professor’s last name or the year it was offered.

1.  **Push Indents to Left**

>   This function will decrease the indents of all module items until one of the
>   items hits the leftmost margin of the module.

1.  **Fix Single Question Quiz Groups**

>   This function will extract single questions outside their question group if
>   it is the only question in its group. The extracted question will take on
>   the point value of the question group it left. The empty question group will
>   be deleted afterwards.

1.  **Remove Page Title Numbering**

>   This function will remove the numbering that occurs when page titles have
>   the same name (for example, test and test-2)

1.  There is also a help button on the top-right corner of the program which
    contains a short description for each function.

![](media/63fe3177b1fe9192ab37173f931f95ad.png)

1.  If you click on any one of the buttons, the message box at the bottom on the
    window will change. A spinning icon will appear and the console will begin
    printing out messages to indicate that the program is successfully running.

>   **NOTE**: If you need to force stop the program, exit the user interface and
>   console by closing both windows.

>   **IMPORTANT:** *DO NOT* click any other buttons during this time while the
>   program is running.

![](media/6a335e1730d6d14f0181308db4627f60.png)

1.  Once the program runs successfully, the message box will say “**done**”. At
    this time, you can call another function by clicking on another button.

![](media/f49c3c38155e1dd75c0e92f01d996f8c.png)

>   C:\\Users\\Andre\\Desktop\\hohohoho2.png

>   USE CASES

1.  FORGET ACCESS TOKEN

>   If another person wants to enter their credentials and run the program under
>   their account, forgetting the Access Token will delete the file holding the
>   old Access Token and prompt a user for a new Access Token upon the next
>   login.

>   **NOTE**: If you regenerate your Access Token on Canvas without forgetting
>   the Access Token, the program will try to read your old Access Token file
>   upon your next login and it will encounter an error. To fix this issue, you
>   will need to delete the file called “deets” located in the same directory as
>   the program.

![](media/b6c08d5803526c3a598f2aefabafc9da.png)

1.  DELETE ALL CONTENT

>   If you need to reset a course without changing the course ID, please choose
>   this option.

1.  REVERT PAGES TO FIRST VERSION

>   This reverts all pages to its initial version before any edits were made.
>   This is useful after converting HTMLs to pages because users will have a
>   snapshot of their course after the conversion.

1.  CONVERT HTML TO PAGES

>   All HTMLs exported from Blackboard Learn and imported into Canvas will show
>   up as attachments. This function will convert all HTMLs from ‘Attachment’
>   type to ‘Page’ type. It will also fix all page-to-page links and
>   page-to-file/image links associated with these HTMLs. In other words, if an
>   HTML is linked to another HTML, file, or image, a converted HTML page will
>   now link to another converted HTML page, file, or image.

1.  DELETE EXCESS CONTENT

>   After exporting from Blackboard Learn and importing into Canvas, some excess
>   assignments, assignment groups, and announcements may also be transferred
>   over. These assignments and assignments groups are specifically named
>   “Program”, “Majors”, “Year Level”, “Faculty”, “Minors”, “Term”, “Linked
>   Section”, “Discussion”, “Lab”, “Program Year”, “Section”, “Status”, and
>   “Tutorial”. Empty announcements may also be migrated over. This function
>   will remove all these elements.

1.  TRY ANOTHER COURSE

>   Cleaning up multiple courses may be a hassle if the program constantly needs
>   to be closed and reopened every time you want to switch courses. This will
>   allow you to switch courses within the program.

1.  EXTERNAL LINKS TO NEW TABS

>   Sometimes external links are not rendered because they are inaccessible from
>   Canvas’ servers. Therefore, it is a better idea to always load external
>   links in new tabs. Running this function will modify all external URLs under
>   Modules to load in new tabs.

1.  MASS MOVE ITEMS TO MODULE

>   Since Canvas can only nest items two levels deep under Modules (the actual
>   module and the module items that sit within it), content imported from
>   Connect all be thrown into a single module with indents acting as deeper
>   levels of nesting. This can look very overwhelming for the end-user. It is
>   better to separate deeper nested items into separate modules. After creating
>   these separate modules, it may be tedious to move items into them by
>   dragging and dropping one-by-one. This function allows users to move items
>   all at once to a specific module of their choice.

1.  PUBLISH ALL

    This function will publish all modules and items under Modules in the
    course. Canvas has trouble identifying hidden and visible links in Connect
    and makes its own judgment call to publish or not publish certain items
    after importing. Publishing all items makes everything consistent, so the
    instructor of the course can unpublish any undesired items after the
    clean-up.

2.  DELETE FIRST TEXT HEADER

    Since folders/modules in Connect can hold metadata, Canvas will sometimes
    create a page or a text header that sits as the first item in a module and
    has the same title as that module. Indeed, if it is a page, it may contain
    some important information about the module so deleting it would be
    problematic. However, if it is a text header, it will not hold any
    additional information about the module, so deleting it would be ideal.

3.  CORRECT COURSE NAME AND COURSE CODE

    Course names that follow the structure: [MG] [Name of Course] [Year Offered]
    – [Professor’s last name], may have some missing information; usually the
    year offered or professor’s last name. This function parses the course name
    and checks if the year offered or professor’s last is included. If not, it
    will prompt the user for the information. It will then update the Course
    name and Course Code of the course automatically.

4.  PUSH INDENTS TO LEFT

    After moving around module items in the course, the indentation of the
    module items may not consistently sit on the left margin of the module. This
    function will decrease the indentation of all items in a module until an
    item hits the leftmost margin of the module. This will retain the overall
    structure of the module and reduces the number of clicks needed to decrease
    the indentation of every module item manually.

5.  FIX SINGLE QUESTION QUIZ GROUPS

    Exporting quizzes from Connect and importing them into Canvas has always
    yielded some issues. One of these issues include question groups in quizzes
    that only hold a single question in them. This moves all single questions in
    a single question group outside the question group and then deletes the
    empty question group afterwards. The extracted question will also take the
    point value specified in its question group. This is useful because it
    cleans up the quiz questions and maintains the order of the questions when
    it was imported.

6.  REMOVE PAGE TITLE NUMBERING

    Canvas does not allow identical page titles. If two different pages have
    identical page titles, Canvas will add numbering at the end of one of the
    page titles to distinguish it from the other. This function will replace the
    numbering with spaces, so visually, page title names will look identical.
    This is useful because running HTML to Pages sometimes converts html files
    that have the same name as existing Canvas Pages. Running this function
    effectively allows for page titles to visually have the same name.

>   EXAMPLE: RUNNING THE PROGRAM FOR AN HTML-HEAVY COURSE

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
