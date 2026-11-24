from __future__ import annotations
from pydantic import BaseModel
from .cloud_watch_managed_rule import CloudWatchManagedRule


class CloudWatchPutManagedInsightRulesRequest(BaseModel):
    ManagedRules: list[CloudWatchManagedRule]
