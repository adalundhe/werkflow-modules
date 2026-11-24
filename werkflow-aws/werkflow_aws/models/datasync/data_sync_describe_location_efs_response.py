from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_sync_ec2_config import DataSyncEc2Config


class DataSyncDescribeLocationEfsResponse(BaseModel):
    LocationArn: StrictStr | None = None
    LocationUri: StrictStr | None = None
    Ec2Config: DataSyncEc2Config | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    AccessPointArn: StrictStr | None = None
    FileSystemAccessRoleArn: StrictStr | None = None
    InTransitEncryption: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
