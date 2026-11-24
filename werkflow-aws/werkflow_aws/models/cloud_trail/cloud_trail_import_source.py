from __future__ import annotations
from pydantic import BaseModel
from .cloud_trail_s3_import_source import CloudTrailS3ImportSource


class CloudTrailImportSource(BaseModel):
    S3: CloudTrailS3ImportSource | None = None
