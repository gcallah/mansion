from unittest.mock import patch

import dashboard.cl_dash_board as cldb


def test_create_cl_dash_board():
    db = cldb.CLDashboard(cldb.TEST_MENU)
    assert isinstance(db, cldb.CLDashboard)


@patch('textapp.text_app.get_choice', return_value=cldb.EXIT, autospec=True)
def test_run(mock_get_choice):
    db = cldb.CLDashboard(cldb.TEST_MENU)
    assert db.run() == cldb.SUCCESS

