# Course Cleanup Script

## Introduction

The purpose of this script is to clean up courses that have been exported from Connect and imported into Canvas. It automates tasks that would otherwise take a long time to do manually using the Canvas user interface.

## Main Features
- Resetting the course without changing the course code
- Deleting excess announcements, assignments, and assignment groups that may have migrated over from Connect.
- Reverting all pages to their original version.
- Converts HTML files into pages within Canvas and fixes page to page links associated with those converted pages.
- Fixes broken links between page and images/files.
- and more!

## Requirements
- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installing/)

## Installation
After downloading all the files into a specific directory and navigating into that directory, ensure you have [Python 3.x](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/) installed before running the following commands:
```sh
pip install -r requirements.txt
python main_app.py
```
You should be prompted with a window asking for a course code and an access token. The script is now running.