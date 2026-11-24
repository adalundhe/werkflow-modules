from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .ecs_session import ECSSession


class ECSExecuteCommandResponse(BaseModel):
    clusterArn: StrictStr | None = None
    containerArn: StrictStr | None = None
    containerName: StrictStr | None = None
    interactive: StrictBool | None = None
    session: ECSSession | None = None
    taskArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
