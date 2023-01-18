import os
import webview
import webview.menu as wm


class Api:
    def fullscreen(self):
        webview.windows[0].toggle_fullscreen()

    def save_content(self, content):
        filename = webview.windows[0].create_file_dialog(webview.SAVE_DIALOG)
        if not filename:
            return

        with open(filename, 'w') as f:
            f.write(content)

    def test(self):
        print('test...')
        return


class Menu:
    def click_me():
        active_window = webview.active_window()
        if active_window:
            active_window.load_html('<h1>You clicked me!</h1>')

    def open_file_dialog():
        active_window = webview.active_window()
        active_window.create_file_dialog(
            webview.SAVE_DIALOG, directory='/', save_filename='test.file')

    def change_active_window_content():
        active_window = webview.active_window()
        if active_window:
            active_window.load_html('<h1>You changed this window!</h1>')


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
    api = Api()
    window = webview.create_window(
        'pywebview-vue boilerplate', entry, js_api=api)

    menu_items = [
        wm.Menu(
            'Test Menu',
            [
                wm.MenuAction('Change Active Window Content',
                              Menu.change_active_window_content),
                wm.MenuSeparator(),
                wm.Menu(
                    'Random',
                    [
                        wm.MenuAction('Click Me', Menu.click_me),
                        wm.MenuAction('File Dialog', Menu.open_file_dialog)
                    ]
                )
            ]
        )
    ]

    webview.start(menu=menu_items, debug=True)
    # webview.start(debug=True)
