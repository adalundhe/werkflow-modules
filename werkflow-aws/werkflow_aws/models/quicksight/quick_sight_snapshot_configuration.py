from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_parameters import QuickSightParameters
from .quick_sight_snapshot_destination_configuration import QuickSightSnapshotDestinationConfiguration
from .quick_sight_snapshot_file_group import QuickSightSnapshotFileGroup


class QuickSightSnapshotConfiguration(BaseModel):
    FileGroups: list[QuickSightSnapshotFileGroup] | None = None
    DestinationConfiguration: QuickSightSnapshotDestinationConfiguration | None = None
    Parameters: QuickSightParameters | None = None
