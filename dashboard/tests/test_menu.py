import pytest

import dashboard.menu as menu


def test_create_menu():
    # Test that the menu is created correctly
    test_menu = menu.Menu(menu.TEST_MENU)
    assert isinstance(test_menu, menu.Menu)
    for key in menu.REQ_KEYS:
        assert key in test_menu


def test_to_dict():
    # Test that the menu can be converted to JSON
    test_menu = menu.Menu(menu.TEST_MENU)
    menu_dict = test_menu.to_dict()
    assert(menu_dict == menu.TEST_MENU)
