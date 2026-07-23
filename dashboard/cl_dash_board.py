from dashboard.dash_board import Dashboard


class CLDashboard(Dashboard):
    def __init__(self, menu: str):
        self.menu = menu
