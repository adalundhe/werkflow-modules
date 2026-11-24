from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexDescribeExportRequest(BaseModel):
    exportId: StrictStr
