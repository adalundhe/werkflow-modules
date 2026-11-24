from __future__ import annotations
from pydantic import BaseModel
from .data_sync_s3_manifest_config import DataSyncS3ManifestConfig


class DataSyncSourceManifestConfig(BaseModel):
    S3: DataSyncS3ManifestConfig | None = None
