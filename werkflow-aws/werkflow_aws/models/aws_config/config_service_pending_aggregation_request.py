from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServicePendingAggregationRequest(BaseModel):
    RequesterAccountId: StrictStr | None = None
    RequesterAwsRegion: StrictStr | None = None
