from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ecs_express_gateway_service_configuration import ECSExpressGatewayServiceConfiguration
from .ecs_express_gateway_service_status import ECSExpressGatewayServiceStatus


class ECSUpdatedExpressGatewayService(BaseModel):
    serviceArn: StrictStr | None = None
    cluster: StrictStr | None = None
    serviceName: StrictStr | None = None
    status: ECSExpressGatewayServiceStatus | None = None
    targetConfiguration: ECSExpressGatewayServiceConfiguration | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
