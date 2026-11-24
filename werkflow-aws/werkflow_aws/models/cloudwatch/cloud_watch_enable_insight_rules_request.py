from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchEnableInsightRulesRequest(BaseModel):
    RuleNames: list[StrictStr]
