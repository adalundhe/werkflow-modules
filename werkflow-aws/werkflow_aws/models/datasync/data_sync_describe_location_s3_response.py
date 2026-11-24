from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_sync_s3_config import DataSyncS3Config


class DataSyncDescribeLocationS3Response(BaseModel):
    LocationArn: StrictStr | None = None
    LocationUri: StrictStr | None = None
    S3StorageClass: StrictStr | None = None
    S3Config: DataSyncS3Config | None = None
    AgentArns: list[StrictStr] | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
