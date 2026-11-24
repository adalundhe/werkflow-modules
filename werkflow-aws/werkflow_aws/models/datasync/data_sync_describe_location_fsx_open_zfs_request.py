from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncDescribeLocationFsxOpenZfsRequest(BaseModel):
    LocationArn: StrictStr
