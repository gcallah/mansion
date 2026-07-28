
"""
Module creates an object with vetted menu info.
"""
import textapp.text_app as tapp
from textapp.text_app import SUCCESS, EXIT  # noqa 401

REQ_KEYS = [tapp.TYPE, tapp.CHOICES]

MAIN_MENU = 'Test'

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


class Menu:
    """
    Class to create a menu object from a dictionary.
    """
    def __init__(self, menu_dict: dict):
        if not isinstance(menu_dict, dict):
            raise TypeError("Menu must be initialized with a dictionary.")
        for key in REQ_KEYS:
            if key not in menu_dict:
                raise ValueError(f"Missing required key: {key}")
        self.menu_dict = menu_dict

    def to_dict(self) -> dict:
        """
        Returns the menu dictionary.
        """
        return self.menu_dict

    def __contains__(self, item):
        """
        Checks if a key is in the menu dictionary.
        """
        return item in self.menu_dict


def main():
    """
    Main function to test the Menu class.
    """
    menu = Menu(TEST_MENU)
    print(menu.to_json())


if __name__ == "__main__":
    main()
