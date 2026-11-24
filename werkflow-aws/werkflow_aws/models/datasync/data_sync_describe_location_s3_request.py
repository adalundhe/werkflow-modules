from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncDescribeLocationS3Request(BaseModel):
    LocationArn: StrictStr
