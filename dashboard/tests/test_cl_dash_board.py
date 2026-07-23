import dashboard.cl_dash_board as cldb


def test_create_cl_dash_board():
    db = cldb.CLDashboard('some string')
    assert isinstance(db, cldb.CLDashboard)
