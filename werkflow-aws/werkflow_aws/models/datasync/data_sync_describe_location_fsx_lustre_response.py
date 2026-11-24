from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class DataSyncDescribeLocationFsxLustreResponse(BaseModel):
    LocationArn: StrictStr | None = None
    LocationUri: StrictStr | None = None
    SecurityGroupArns: list[StrictStr] | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
