from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchDeleteQuotaShareRequest(BaseModel):
    quotaShareArn: StrictStr
