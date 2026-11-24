from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ecs_service_connect_test_traffic_rules import ECSServiceConnectTestTrafficRules


class ECSServiceConnectClientAlias(BaseModel):
    port: StrictInt | None = None
    dnsName: StrictStr | None = None
    testTrafficRules: ECSServiceConnectTestTrafficRules | None = None
