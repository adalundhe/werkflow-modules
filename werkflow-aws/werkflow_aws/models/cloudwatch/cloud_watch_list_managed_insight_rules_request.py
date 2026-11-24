from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchListManagedInsightRulesRequest(BaseModel):
    ResourceARN: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
