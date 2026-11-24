from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_user_bucket import EC2UserBucket


class EC2ImageDiskContainer(BaseModel):
    Description: StrictStr | None = None
    DeviceName: StrictStr | None = None
    Format: StrictStr | None = None
    SnapshotId: StrictStr | None = None
    Url: StrictStr | None = None
    UserBucket: EC2UserBucket | None = None
