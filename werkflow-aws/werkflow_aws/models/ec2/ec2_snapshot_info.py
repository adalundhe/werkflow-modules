from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2SnapshotInfo(BaseModel):
    Description: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    Encrypted: StrictBool | None = None
    VolumeId: StrictStr | None = None
    State: StrictStr | None = None
    VolumeSize: StrictInt | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    Progress: StrictStr | None = None
    OwnerId: StrictStr | None = None
    SnapshotId: StrictStr | None = None
    OutpostArn: StrictStr | None = None
    SseType: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
