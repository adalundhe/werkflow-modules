from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_update_s3_bucket_resource import GuardDutyUpdateS3BucketResource


class GuardDutyUpdateProtectedResource(BaseModel):
    S3Bucket: GuardDutyUpdateS3BucketResource | None = None
