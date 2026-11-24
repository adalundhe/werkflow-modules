from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ecs_network_binding import ECSNetworkBinding


class ECSContainerStateChange(BaseModel):
    containerName: StrictStr | None = None
    imageDigest: StrictStr | None = None
    runtimeId: StrictStr | None = None
    exitCode: StrictInt | None = None
    networkBindings: list[ECSNetworkBinding] | None = None
    reason: StrictStr | None = None
    status: StrictStr | None = None
