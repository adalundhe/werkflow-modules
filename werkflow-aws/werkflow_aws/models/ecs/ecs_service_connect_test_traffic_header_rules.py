from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_service_connect_test_traffic_header_match_rules import ECSServiceConnectTestTrafficHeaderMatchRules


class ECSServiceConnectTestTrafficHeaderRules(BaseModel):
    name: StrictStr | None = None
    value: ECSServiceConnectTestTrafficHeaderMatchRules | None = None
