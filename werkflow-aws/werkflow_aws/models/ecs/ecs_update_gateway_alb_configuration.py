from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .ecs_gateway_alb_test_traffic_rules import ECSGatewayAlbTestTrafficRules
from .ecs_gateway_elb_access_log_configuration import ECSGatewayElbAccessLogConfiguration
from .ecs_update_gateway_network_configuration import ECSUpdateGatewayNetworkConfiguration


class ECSUpdateGatewayAlbConfiguration(BaseModel):
    networkConfiguration: ECSUpdateGatewayNetworkConfiguration | None = None
    maxAlbCount: StrictInt | None = None
    webACLArn: StrictStr | None = None
    accessLogs: ECSGatewayElbAccessLogConfiguration | None = None
    httpDesync: Literal['monitor', 'defensive', 'strictest'] | None = None
    testTrafficRules: ECSGatewayAlbTestTrafficRules | None = None
