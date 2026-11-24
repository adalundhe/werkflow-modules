from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecs_daemon_task_definition_summary import ECSDaemonTaskDefinitionSummary


class ECSListDaemonTaskDefinitionsResponse(BaseModel):
    daemonTaskDefinitions: list[ECSDaemonTaskDefinitionSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
