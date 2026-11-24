from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_tag import EC2Tag


class EC2Snapshot(BaseModel):
    SnapshotId: StrictStr | None = None
    VolumeId: StrictStr | None = None
    State: StrictStr | None = None
    StateMessage: StrictStr | None = None
    StartTime: datetime.datetime | None = None
    Progress: StrictStr | None = None
    OwnerId: StrictStr | None = None
    Description: StrictStr | None = None
    VolumeSize: StrictInt | None = None
    Encrypted: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
    Tags: list[EC2Tag] | None = None
