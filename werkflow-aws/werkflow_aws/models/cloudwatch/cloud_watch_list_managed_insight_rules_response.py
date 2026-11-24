from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_managed_rule_description import CloudWatchManagedRuleDescription


class CloudWatchListManagedInsightRulesResponse(BaseModel):
    ManagedRules: list[CloudWatchManagedRuleDescription] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
