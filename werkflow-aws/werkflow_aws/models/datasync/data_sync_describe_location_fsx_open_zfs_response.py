from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_sync_fsx_protocol import DataSyncFsxProtocol


class DataSyncDescribeLocationFsxOpenZfsResponse(BaseModel):
    LocationArn: StrictStr | None = None
    LocationUri: StrictStr | None = None
    SecurityGroupArns: list[StrictStr] | None = None
    Protocol: DataSyncFsxProtocol | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
