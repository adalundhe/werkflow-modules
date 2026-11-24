from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ecs_service_connect_client_alias import ECSServiceConnectClientAlias
from .ecs_service_connect_tls_configuration import ECSServiceConnectTlsConfiguration
from .ecs_timeout_configuration import ECSTimeoutConfiguration


class ECSServiceConnectService(BaseModel):
    portName: StrictStr | None = None
    discoveryName: StrictStr | None = None
    clientAliases: list[ECSServiceConnectClientAlias] | None = None
    ingressPortOverride: StrictInt | None = None
    timeout: ECSTimeoutConfiguration | None = None
    tls: ECSServiceConnectTlsConfiguration | None = None
