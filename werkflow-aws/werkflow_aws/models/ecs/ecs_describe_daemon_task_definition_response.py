from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecs_daemon_task_definition import ECSDaemonTaskDefinition


class ECSDescribeDaemonTaskDefinitionResponse(BaseModel):
    daemonTaskDefinition: ECSDaemonTaskDefinition | None = None
    ResponseMetadata: dict[str, Any] | None = None
