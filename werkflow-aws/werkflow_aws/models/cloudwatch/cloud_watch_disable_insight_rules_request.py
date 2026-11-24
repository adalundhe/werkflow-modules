from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchDisableInsightRulesRequest(BaseModel):
    RuleNames: list[StrictStr]
