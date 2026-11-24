from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ecs_network_binding import ECSNetworkBinding


class ECSSubmitContainerStateChangeRequest(BaseModel):
    cluster: StrictStr | None = None
    task: StrictStr | None = None
    containerName: StrictStr | None = None
    runtimeId: StrictStr | None = None
    status: StrictStr | None = None
    exitCode: StrictInt | None = None
    reason: StrictStr | None = None
    networkBindings: list[ECSNetworkBinding] | None = None
