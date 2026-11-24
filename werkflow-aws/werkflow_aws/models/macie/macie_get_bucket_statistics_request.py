from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieGetBucketStatisticsRequest(BaseModel):
    accountId: StrictStr | None = None
