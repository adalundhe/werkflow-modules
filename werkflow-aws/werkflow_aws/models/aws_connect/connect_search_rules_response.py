from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_rule_search_summary import ConnectRuleSearchSummary


class ConnectSearchRulesResponse(BaseModel):
    Rules: list[ConnectRuleSearchSummary] | None = None
    ApproximateTotalCount: StrictInt | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
