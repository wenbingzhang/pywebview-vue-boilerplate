import webview
import webview.menu as wm
from os.path import expanduser

class Menu:
    def click_me():
        active_window = webview.active_window()
        if active_window:
            active_window.load_html('<h1>You clicked me!</h1>')

    def open_file_dialog():
        active_window = webview.active_window()
        active_window.create_file_dialog(
            webview.OPEN_DIALOG, directory=expanduser("~"))

    def change_active_window_content():
        active_window = webview.active_window()
        if active_window:
            active_window.load_html('<h1>You changed this window!</h1>')

    def Get():
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
                            wm.MenuAction(
                                'File Dialog', Menu.open_file_dialog)
                        ]
                    )
                ]
            )
        ]
        return menu_items
