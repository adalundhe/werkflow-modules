from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncDescribeTaskRequest(BaseModel):
    TaskArn: StrictStr
