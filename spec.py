""" 
work flow: get text content like "23.34239.394"(wistron PN format) from
clipboard, making a GET request using requests, with URL parameter
PartNumber=text, and then open its html text with webbrowser module.
"""

import ctypes
import requests
import os
import webbrowser

def spec():
    # clipboard format TEXT defined by MS
    CF_TEXT = 1

    kernel32 = ctypes.windll.kernel32
    user32 = ctypes.windll.user32

    user32.OpenClipboard(0)
    if user32.IsClipboardFormatAvailable(CF_TEXT):
        data = user32.GetClipboardData(CF_TEXT)
        data_locked = kernel32.GlobalLock(data)
        text = ctypes.c_char_p(data_locked)
        print(text.value)
        kernel32.GlobalUnlock(data_locked)
    else:
        print('no text in clipboard')
    user32.CloseClipboard()

    # decode bytes to unicode string
    s = text.value.decode()

    # fork a browser GET request
    url = 'http://wpqssvr.wistron.com.tw:7001/wpqs/servlet/COM.qpart.Attachment'
    para = {'PartNumber': s}
    h = {
        'Accept': 'text/html',
        'Connection': 'keep-alive',
        'Host': 'wpqssvr.wistron.com.tw:7001',
        'Accept-Language': 'zh-TW',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0;rv:11.0) like Gecko'
    }

    # make the request and stores the html into temp file, open with IE
    try:
        r = requests.get(url, params = para, headers=h)
        path = os.path.abspath('temp.html')
        url = 'file://' + path
        with open(path, 'w') as f:
            f.write(r.text)
        webbrowser.open(url)
    except:
        print('open url or open file fails')
        raise

    exit()

if __name__ == '__main__':
    spec()
