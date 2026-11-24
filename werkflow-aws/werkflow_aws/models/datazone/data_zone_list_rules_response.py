from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_rule_summary import DataZoneRuleSummary


class DataZoneListRulesResponse(BaseModel):
    items: list[DataZoneRuleSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
