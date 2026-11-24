from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConfigServiceDescribePendingAggregationRequestsRequest(BaseModel):
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
