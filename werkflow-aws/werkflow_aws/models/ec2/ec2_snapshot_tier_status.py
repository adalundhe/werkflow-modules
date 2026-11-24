from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2SnapshotTierStatus(BaseModel):
    SnapshotId: StrictStr | None = None
    VolumeId: StrictStr | None = None
    Status: StrictStr | None = None
    OwnerId: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    StorageTier: StrictStr | None = None
    LastTieringStartTime: datetime.datetime | StrictStr | None = None
    LastTieringProgress: StrictInt | None = None
    LastTieringOperationStatus: StrictStr | None = None
    LastTieringOperationStatusDetail: StrictStr | None = None
    ArchivalCompleteTime: datetime.datetime | StrictStr | None = None
    RestoreExpiryTime: datetime.datetime | StrictStr | None = None
