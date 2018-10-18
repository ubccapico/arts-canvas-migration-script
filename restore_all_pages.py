import api_calls as api


def restore_page(page_name, page_url):
    # version #1 is always the first version of a page, hence the constant
    # argument 1
    revision = api.revert_to_page_revision(page_url, 1)
    print('{} restored'.format(page_name))
    return


def master_rap():
    pages = api.get_all_pages()
    for page in pages:
        restore_page(page['title'], page['url'])
    print('Done Reverting All Pages to First Version!')
    return
