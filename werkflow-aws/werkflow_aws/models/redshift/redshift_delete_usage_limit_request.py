from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftDeleteUsageLimitRequest(BaseModel):
    UsageLimitId: StrictStr
