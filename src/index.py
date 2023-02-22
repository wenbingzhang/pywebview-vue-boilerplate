import os
import webview
import webview.menu as wm
from pyapp.api import JsApi
from pyapp.menu import Menu
from pyapp.hotkey import HotKey


def get_entrypoint():
    def exists(path):
        return os.path.exists(os.path.join(os.path.dirname(__file__), path))

    if exists('../gui/index.html'):  # unfrozen development
        return '../gui/index.html'

    if exists('../Resources/gui/index.html'):  # macos
        return '../Resources/gui/index.html'

    if exists('./gui/index.html'):
        return './gui/index.html'

    raise Exception('No index.html found')


entry = get_entrypoint()

if __name__ == '__main__':
    HotKey.Init()

    api = JsApi()
    window = webview.create_window(
        'pywebview-vue boilerplate', entry, js_api=api)

    webview.start(menu=Menu.Get(), debug=True)
    # webview.start(debug=True)
