import textapp.text_app as tapp

import dashboard.menu as menu
from dashboard.menu import SUCCESS, EXIT  # noqa 401
from dashboard.dash_board import Dashboard


def word_count():  # text: str) -> int:
    """Count the number of words in a string."""
    return 0
    # return len(text.split())


MAIN_MENU = 'Welcome to the Mansion dashboard.'
WORD_COUNT = 'W'

TOP_MENU = {
    tapp.TYPE: tapp.MENU,
    tapp.TITLE: MAIN_MENU,
    tapp.DEFAULT: WORD_COUNT,
    tapp.CHOICES: {
        WORD_COUNT: {tapp.FUNC: word_count,
                     tapp.TEXT: "Word count"},
        EXIT: {tapp.FUNC: tapp.exit,
               tapp.TEXT: "Exit", },
    },
}


top_menu = menu.Menu(TOP_MENU)


class CLDashboard(Dashboard):
    def __init__(self, menu_obj: menu.Menu):
        if not isinstance(menu_obj, menu.Menu):
            raise TypeError('menu must be a Menu object')
        self.menu = menu_obj

    def run(self):
        return tapp.run_menu_cont(self.menu.to_dict())


def main():
    cldash = CLDashboard(top_menu)
    cldash.run()


if __name__ == "__main__":
    main()
