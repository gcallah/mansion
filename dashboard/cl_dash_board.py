import textapp.text_app as tapp

from dashboard.dash_board import Dashboard


class CLDashboard(Dashboard):
    def __init__(self, menu: str):
        self.menu = menu


def main():
    # Running form in test mode needs to be fixed!
    ret = tapp.data_repr(tapp.TEST_DATA)
    print(tapp.fmt.text(ret[tapp.DATA_TEXT]))
    if tapp.mode == tapp.PROD:
        mod_form = tapp.run_form(tapp.TEST_FORM)
        # only the field values will go back to the server:
        form_info = f"The modified form is: {mod_form[tapp.FLDS]}"
        print(tapp.fmt.menu_choice(form_info))
    return tapp.run_menu_cont(tapp.TEST_MENU)


if __name__ == "__main__":
    main()
