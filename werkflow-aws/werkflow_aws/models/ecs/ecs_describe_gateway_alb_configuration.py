from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ecs_gateway_alb_test_traffic_rules import ECSGatewayAlbTestTrafficRules
from .ecs_gateway_elb_access_log_configuration import ECSGatewayElbAccessLogConfiguration
from .ecs_gateway_elb_network_configuration import ECSGatewayElbNetworkConfiguration


class ECSDescribeGatewayAlbConfiguration(BaseModel):
    networkConfiguration: ECSGatewayElbNetworkConfiguration | None = None
    scheme: StrictStr | None = None
    accessLogs: ECSGatewayElbAccessLogConfiguration | None = None
    webACLArn: StrictStr | None = None
    port: StrictInt | None = None
    protocol: StrictStr | None = None
    maxAlbCount: StrictInt | None = None
    currentAlbCount: StrictInt | None = None
    httpDesync: StrictStr | None = None
    testTrafficRules: ECSGatewayAlbTestTrafficRules | None = None
