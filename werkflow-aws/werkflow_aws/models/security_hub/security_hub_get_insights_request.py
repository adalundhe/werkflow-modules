from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubGetInsightsRequest(BaseModel):
    InsightArns: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
