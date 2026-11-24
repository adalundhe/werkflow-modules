from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ecs_express_gateway_service_configuration import ECSExpressGatewayServiceConfiguration
from .ecs_express_gateway_service_status import ECSExpressGatewayServiceStatus
from .ecs_tag import ECSTag


class ECSExpressGatewayService(BaseModel):
    cluster: StrictStr | None = None
    serviceName: StrictStr | None = None
    serviceArn: StrictStr | None = None
    infrastructureRoleArn: StrictStr | None = None
    status: ECSExpressGatewayServiceStatus | None = None
    currentDeployment: StrictStr | None = None
    activeConfigurations: list[ECSExpressGatewayServiceConfiguration] | None = None
    tags: list[ECSTag] | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
