import psutil
from typing import Iterator, Union, Dict
from werkflow_system.exceptions import MissingVolumeException
from .drive import Drive


class DriveGroup:

    def __init__(self) -> None:
        self._drives: Dict[str, Drive] = {}
        self._mountpoints: Dict[str, Drive] = {}
        self._populate_drives()

    def _populate_drives(self) -> None:
        try:
            drives = psutil.disk_partitions()
        except OSError:
            drives = []

        for partition in drives:
            drive = Drive(partition)
            if not drive.mounted:
                continue
            if partition.device not in self._drives:
                self._drives[partition.device] = drive
            self._mountpoints[partition.mountpoint] = drive

    def __iter__(self) -> Iterator[Drive]:
        yield from self._mountpoints.values()

    def list(self) -> Iterator[str]:
        yield from self._drives.keys()

    def __getitem__(self, drive_name: str) -> Drive:
        return self.get(drive_name)

    def get(self, drive_name: str) -> Drive:
        drive = self._drives.get(drive_name)
        if drive is None:
            raise MissingVolumeException(
                list(self._drives.keys())
            )

        return drive

    def exists(self, drive_name: str) -> bool:
        return self._drives.get(drive_name) is not None

    def all_like(self, search_drive_name: str) -> Iterator[Drive]:
        for drive_name, drive in self._drives.items():
            if search_drive_name in drive_name:
                yield drive

    def like(self, search_drive_name: str) -> Union[Drive, None]:
        for drive_name, drive in self._drives.items():
            if search_drive_name in drive_name:
                return drive

        return None

    def update(self) -> None:
        try:
            drives = psutil.disk_partitions()
        except OSError:
            drives = []

        active_mountpoints = set()
        active_devices = set()

        for partition in drives:
            existing = self._mountpoints.get(partition.mountpoint)
            if existing is None:
                drive = Drive(partition)
            else:
                existing.update()
                drive = existing

            if not drive.mounted:
                continue

            active_mountpoints.add(partition.mountpoint)
            active_devices.add(partition.device)
            self._mountpoints[partition.mountpoint] = drive
            if partition.device not in self._drives:
                self._drives[partition.device] = drive

        for mountpoint in list(self._mountpoints.keys()):
            if mountpoint not in active_mountpoints:
                del self._mountpoints[mountpoint]

        for device in list(self._drives.keys()):
            if device not in active_devices:
                del self._drives[device]

    def at_path(self, path: str) -> Drive:
        drive = self._mountpoints.get(path)
        if drive is not None:
            return drive

        raise MissingVolumeException(
            list(self._drives.keys())
        )

    def at_path_like(self, path: str) -> Iterator[Drive]:
        for drive in self._mountpoints.values():
            if path in drive.path:
                yield drive
