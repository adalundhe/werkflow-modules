from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_policy_grant_member import DataZonePolicyGrantMember


class DataZoneListPolicyGrantsResponse(BaseModel):
    grantList: list[DataZonePolicyGrantMember] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
