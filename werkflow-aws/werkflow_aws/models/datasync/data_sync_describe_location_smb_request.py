from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncDescribeLocationSmbRequest(BaseModel):
    LocationArn: StrictStr
