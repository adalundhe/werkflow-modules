from __future__ import annotations
from pydantic import BaseModel
from .macie_s3_bucket import MacieS3Bucket
from .macie_s3_object import MacieS3Object


class MacieResourcesAffected(BaseModel):
    s3Bucket: MacieS3Bucket | None = None
    s3Object: MacieS3Object | None = None
