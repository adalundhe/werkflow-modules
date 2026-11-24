import psutil
from typing import Any
from .data_amount import DataAmount


class Drive:

    def __init__(self, drive_stats: Any) -> None:
        self.path: str = drive_stats.mountpoint
        self.name: str = drive_stats.device
        self.type: str = drive_stats.fstype
        self.options: str = drive_stats.opts
        self._mounted: bool = False

        self.total = DataAmount(0)
        self.used = DataAmount(0)
        self.available = DataAmount(0)
        self.percentage_used: float = 0.0

        self.update()

    @property
    def mounted(self) -> bool:
        return self._mounted and self.path is not None

    def update(self) -> None:
        if not self.path:
            self._mounted = False
            return

        try:
            disk_usage = psutil.disk_usage(self.path)
            self.total = DataAmount(disk_usage.total)
            self.used = DataAmount(disk_usage.used)
            self.available = DataAmount(disk_usage.free)
            self.percentage_used = disk_usage.percent
            self._mounted = True
        except (PermissionError, FileNotFoundError, OSError):
            self._mounted = False

    @property
    def current_percentage_used(self) -> float:
        self.update()
        return self.percentage_used

    @property
    def current_available(self) -> DataAmount:
        self.update()
        return self.available

    @property
    def current_used(self) -> DataAmount:
        self.update()
        return self.used
