from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ecs_gateway_connector_health_check_matcher import ECSGatewayConnectorHealthCheckMatcher


class ECSGatewayConnectorHealthCheck(BaseModel):
    healthCheckProtocol: StrictStr | None = None
    healthCheckPort: StrictInt | None = None
    healthCheckPath: StrictStr | None = None
    healthCheckTimeoutSeconds: StrictInt | None = None
    healthCheckIntervalSeconds: StrictInt | None = None
    healthyThresholdCount: StrictInt | None = None
    unhealthyThresholdCount: StrictInt | None = None
    matcher: ECSGatewayConnectorHealthCheckMatcher | None = None
