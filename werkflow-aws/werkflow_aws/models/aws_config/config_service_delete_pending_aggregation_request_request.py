from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceDeletePendingAggregationRequestRequest(BaseModel):
    RequesterAccountId: StrictStr
    RequesterAwsRegion: StrictStr
