from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_s3_bucket_configuration import QuickSightS3BucketConfiguration


class QuickSightSnapshotS3DestinationConfiguration(BaseModel):
    BucketConfiguration: QuickSightS3BucketConfiguration | None = None
