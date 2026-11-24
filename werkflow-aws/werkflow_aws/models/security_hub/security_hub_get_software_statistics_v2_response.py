from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .security_hub_group_by_result import SecurityHubGroupByResult


class SecurityHubGetSoftwareStatisticsV2Response(BaseModel):
    GroupByResults: list[SecurityHubGroupByResult] | None = None
    ResponseMetadata: dict[str, Any] | None = None
