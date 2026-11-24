from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchDescribeQuotaShareRequest(BaseModel):
    quotaShareArn: StrictStr
