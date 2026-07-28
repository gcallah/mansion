from unittest.mock import patch
import pytest

import dashboard.cl_dash_board as cldb


def test_create_cl_dash_board():
    db = cldb.CLDashboard(cldb.top_menu)
    assert isinstance(db, cldb.CLDashboard)


def test_create_cl_dash_board_bad_menu_type():
    with pytest.raises(TypeError):
        cldb.CLDashboard('Not a dict!')


@patch('textapp.text_app.get_choice', return_value=cldb.EXIT, autospec=True)
def test_run(mock_get_choice):
    db = cldb.CLDashboard(cldb.top_menu)
    assert db.run() == cldb.SUCCESS
