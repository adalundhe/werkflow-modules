from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncDescribeLocationFsxWindowsRequest(BaseModel):
    LocationArn: StrictStr
