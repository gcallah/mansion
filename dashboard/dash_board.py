
"""
The base class for all dashboards.
"""
from abc import ABC, abstractmethod


class Dashboard(ABC):
    @abstractmethod
    def __init__(self):
        pass
