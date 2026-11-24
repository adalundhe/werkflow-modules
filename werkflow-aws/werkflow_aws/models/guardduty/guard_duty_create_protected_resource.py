from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_create_s3_bucket_resource import GuardDutyCreateS3BucketResource


class GuardDutyCreateProtectedResource(BaseModel):
    S3Bucket: GuardDutyCreateS3BucketResource | None = None
