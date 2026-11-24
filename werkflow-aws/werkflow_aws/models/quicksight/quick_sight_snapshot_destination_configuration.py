from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_snapshot_s3_destination_configuration import QuickSightSnapshotS3DestinationConfiguration


class QuickSightSnapshotDestinationConfiguration(BaseModel):
    S3Destinations: list[QuickSightSnapshotS3DestinationConfiguration] | None = None
