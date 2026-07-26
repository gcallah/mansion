import textapp.text_app as tapp
from textapp.text_app import SUCCESS, EXIT  # noqa 401

from dashboard.dash_board import Dashboard

MAIN_MENU = 'Welcome to the Mansion dashboard.'

TEST_MENU = {
    tapp.TYPE: tapp.MENU,
    tapp.TITLE: MAIN_MENU,
    tapp.DEFAULT: tapp.CONTINUE,
    tapp.CHOICES: {
        tapp.CONTINUE: {tapp.FUNC: tapp.go_on,
                        tapp.TEXT: "Continue displaying menu"},
        EXIT: {tapp.FUNC: tapp.exit,
               tapp.TEXT: "Exit", },
    },
}


class CLDashboard(Dashboard):
    def __init__(self, menu: dict):
        self.menu = menu

    def run(self):
        return tapp.run_menu_cont(self.menu)


def main():
    cldash = CLDashboard(TEST_MENU)
    cldash.run()


if __name__ == "__main__":
    main()
