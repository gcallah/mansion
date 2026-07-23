
"""
Tests for Dashboard class.
"""

import pytest
import dashboard.dash_board as db


def test_dash_board_init():
    with pytest.raises(TypeError):
        db.Dashboard()
