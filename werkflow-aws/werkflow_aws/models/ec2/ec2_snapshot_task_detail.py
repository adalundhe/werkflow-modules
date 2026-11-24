from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .ec2_user_bucket_details import EC2UserBucketDetails


class EC2SnapshotTaskDetail(BaseModel):
    Description: StrictStr | None = None
    DiskImageSize: StrictFloat | StrictInt | None = None
    Encrypted: StrictBool | None = None
    Format: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    Progress: StrictStr | None = None
    SnapshotId: StrictStr | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    Url: StrictStr | None = None
    UserBucket: EC2UserBucketDetails | None = None
