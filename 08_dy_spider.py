

def get_albums_url_dy(self, url):

    browser = spynner.Browser()
    browser.hide()
    try:
        resp = browser.load(url)
    except spynner.SpynnerTimeout:
        browser.wait_load()
    page = browser.html.encode('utf-8')
    pattern = re.compile('<a href=".*?(album_id=\d*).*?"')
    items = re.findall(pattern, page)
    # delete repeats
    urls = []
    album_ids = []
    for i in items:
        if i not in album_ids:
            album_ids.append(i)
    for i in album_ids:
        urls.append('//mm.taobao.com/self/album_photo.htm?user_id=687471686&' + i)

    return urls