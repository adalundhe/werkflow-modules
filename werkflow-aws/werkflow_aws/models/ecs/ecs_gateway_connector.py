from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_gateway_connector_deregistration_delay import ECSGatewayConnectorDeregistrationDelay
from .ecs_gateway_connector_filters import ECSGatewayConnectorFilters
from .ecs_gateway_connector_health_check import ECSGatewayConnectorHealthCheck


class ECSGatewayConnector(BaseModel):
    portName: StrictStr | None = None
    healthCheck: ECSGatewayConnectorHealthCheck | None = None
    filters: ECSGatewayConnectorFilters | None = None
    deregistrationDelay: ECSGatewayConnectorDeregistrationDelay | None = None
