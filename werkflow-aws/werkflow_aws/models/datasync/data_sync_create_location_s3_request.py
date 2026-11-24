from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .data_sync_s3_config import DataSyncS3Config
from .data_sync_tag_list_entry import DataSyncTagListEntry


class DataSyncCreateLocationS3Request(BaseModel):
    S3BucketArn: StrictStr
    S3Config: DataSyncS3Config
    Subdirectory: StrictStr | None = None
    S3StorageClass: Literal['STANDARD', 'STANDARD_IA', 'ONEZONE_IA', 'INTELLIGENT_TIERING', 'GLACIER', 'DEEP_ARCHIVE', 'OUTPOSTS', 'GLACIER_INSTANT_RETRIEVAL'] | None = None
    AgentArns: list[StrictStr] | None = None
    Tags: list[DataSyncTagListEntry] | None = None
