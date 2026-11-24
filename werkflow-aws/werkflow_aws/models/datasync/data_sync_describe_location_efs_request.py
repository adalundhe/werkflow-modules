from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncDescribeLocationEfsRequest(BaseModel):
    LocationArn: StrictStr
