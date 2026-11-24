from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecr_pull_through_cache_rule import ECRPullThroughCacheRule


class ECRDescribePullThroughCacheRulesResponse(BaseModel):
    pullThroughCacheRules: list[ECRPullThroughCacheRule] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
