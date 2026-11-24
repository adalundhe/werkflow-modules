from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncDescribeLocationFsxLustreRequest(BaseModel):
    LocationArn: StrictStr
