from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncDescribeLocationFsxOntapRequest(BaseModel):
    LocationArn: StrictStr
