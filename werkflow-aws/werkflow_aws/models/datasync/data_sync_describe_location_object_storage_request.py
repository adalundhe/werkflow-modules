from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncDescribeLocationObjectStorageRequest(BaseModel):
    LocationArn: StrictStr
