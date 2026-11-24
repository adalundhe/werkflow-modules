from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncDescribeLocationNfsRequest(BaseModel):
    LocationArn: StrictStr
