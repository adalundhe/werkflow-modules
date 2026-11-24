from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubGetInsightResultsRequest(BaseModel):
    InsightArn: StrictStr
