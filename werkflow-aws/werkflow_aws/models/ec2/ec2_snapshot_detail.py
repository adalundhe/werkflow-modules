from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .ec2_user_bucket_details import EC2UserBucketDetails


class EC2SnapshotDetail(BaseModel):
    Description: StrictStr | None = None
    DeviceName: StrictStr | None = None
    DiskImageSize: StrictFloat | StrictInt | None = None
    Format: StrictStr | None = None
    Progress: StrictStr | None = None
    SnapshotId: StrictStr | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    Url: StrictStr | None = None
    UserBucket: EC2UserBucketDetails | None = None
