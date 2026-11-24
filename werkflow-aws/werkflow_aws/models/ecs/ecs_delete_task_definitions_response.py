from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecs_failure import ECSFailure
from .ecs_task_definition import ECSTaskDefinition


class ECSDeleteTaskDefinitionsResponse(BaseModel):
    taskDefinitions: list[ECSTaskDefinition] | None = None
    failures: list[ECSFailure] | None = None
    ResponseMetadata: dict[str, Any] | None = None
