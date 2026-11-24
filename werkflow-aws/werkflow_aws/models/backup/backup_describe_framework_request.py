from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupDescribeFrameworkRequest(BaseModel):
    FrameworkName: StrictStr
