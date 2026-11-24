import os
import psutil


class CPU:

    def __init__(self) -> None:
        logical = psutil.cpu_count(logical=True) or os.cpu_count() or 1
        physical = psutil.cpu_count(logical=False) or logical
        self.physical: int = max(1, physical)
        self.total: int = max(1, logical)
        self.percentage_used: float = psutil.cpu_percent()

    def update(self) -> None:
        self.percentage_used = psutil.cpu_percent()
