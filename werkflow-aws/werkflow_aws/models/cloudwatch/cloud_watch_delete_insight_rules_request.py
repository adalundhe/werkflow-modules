from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchDeleteInsightRulesRequest(BaseModel):
    RuleNames: list[StrictStr]
