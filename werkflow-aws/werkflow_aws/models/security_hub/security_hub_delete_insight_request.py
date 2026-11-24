from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubDeleteInsightRequest(BaseModel):
    InsightArn: StrictStr
