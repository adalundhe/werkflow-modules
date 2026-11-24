from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_rule_summary import ConnectRuleSummary


class ConnectListRulesResponse(BaseModel):
    RuleSummaryList: list[ConnectRuleSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
