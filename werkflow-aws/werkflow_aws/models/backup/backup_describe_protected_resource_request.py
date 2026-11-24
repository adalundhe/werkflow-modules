from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupDescribeProtectedResourceRequest(BaseModel):
    ResourceArn: StrictStr
