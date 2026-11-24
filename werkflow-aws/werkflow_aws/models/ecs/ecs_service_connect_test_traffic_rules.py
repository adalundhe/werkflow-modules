from __future__ import annotations
from pydantic import BaseModel
from .ecs_service_connect_test_traffic_header_rules import ECSServiceConnectTestTrafficHeaderRules


class ECSServiceConnectTestTrafficRules(BaseModel):
    header: ECSServiceConnectTestTrafficHeaderRules | None = None
