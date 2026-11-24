from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecs_task_definition import ECSTaskDefinition


class ECSDeregisterTaskDefinitionResponse(BaseModel):
    taskDefinition: ECSTaskDefinition | None = None
    ResponseMetadata: dict[str, Any] | None = None
