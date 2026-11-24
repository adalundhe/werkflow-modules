from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ecs_log_configuration import ECSLogConfiguration
from .ecs_service_connect_access_log_configuration import ECSServiceConnectAccessLogConfiguration
from .ecs_service_connect_container_configuration import ECSServiceConnectContainerConfiguration
from .ecs_service_connect_service import ECSServiceConnectService


class ECSServiceConnectConfiguration(BaseModel):
    enabled: StrictBool | None = None
    namespace: StrictStr | None = None
    services: list[ECSServiceConnectService] | None = None
    logConfiguration: ECSLogConfiguration | None = None
    accessLogConfiguration: ECSServiceConnectAccessLogConfiguration | None = None
    containerConfigurations: list[ECSServiceConnectContainerConfiguration] | None = None
