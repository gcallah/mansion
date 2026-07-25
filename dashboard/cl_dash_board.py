import textapp.text_app as tapp

from dashboard.dash_board import Dashboard

MAIN_MENU = 'Welcome to the Mansion dashboard.'

TEST_MENU = {
    tapp.TYPE: tapp.MENU,
    tapp.TITLE: MAIN_MENU,
    tapp.DEFAULT: tapp.CONTINUE,
    tapp.CHOICES: {
        tapp.CONTINUE: {tapp.FUNC: tapp.go_on,
                        tapp.TEXT: "Continue displaying menu"},
        tapp.EXIT: {tapp.FUNC: tapp.exit,
                    tapp.TEXT: "Exit", },
    },
}


class CLDashboard(Dashboard):
    def __init__(self):
        print('Starting Command Line Dashboard')

    def run(self):
        return tapp.run_menu_cont(tapp.TEST_MENU)


def main():
    cldash = CLDashboard()
    cldash.run()


if __name__ == "__main__":
    main()
