from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .data_sync_s3_config import DataSyncS3Config


class DataSyncUpdateLocationS3Request(BaseModel):
    LocationArn: StrictStr
    Subdirectory: StrictStr | None = None
    S3StorageClass: Literal['STANDARD', 'STANDARD_IA', 'ONEZONE_IA', 'INTELLIGENT_TIERING', 'GLACIER', 'DEEP_ARCHIVE', 'OUTPOSTS', 'GLACIER_INSTANT_RETRIEVAL'] | None = None
    S3Config: DataSyncS3Config | None = None
