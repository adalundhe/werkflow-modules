from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecs_tag import ECSTag
from .ecs_task_definition import ECSTaskDefinition


class ECSDescribeTaskDefinitionResponse(BaseModel):
    taskDefinition: ECSTaskDefinition | None = None
    tags: list[ECSTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
