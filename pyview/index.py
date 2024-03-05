import os
import webview
# import webview.menu as wm
from app.api import JsApi
from app.menu import Menu
from app.hotkey import HotKey


def get_entrypoint():
    def exists(path):
        return os.path.exists(os.path.join(os.path.dirname(__file__), path))

    if exists('./ui/index.html'):  # unfrozen development
        return './ui/index.html'

    if exists('./Resources/ui/index.html'):  # macos
        return './Resources/ui/index.html'

    raise Exception('No index.html found')


entry = get_entrypoint()

if __name__ == '__main__':
    HotKey.Init()

    api = JsApi()
    window = webview.create_window(
        'pywebview-vue boilerplate', entry, js_api=api)

    webview.start(menu=Menu.Get(), debug=True)
    # webview.start(debug=True)
