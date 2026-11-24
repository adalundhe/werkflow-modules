from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecs_task_set import ECSTaskSet


class ECSUpdateTaskSetResponse(BaseModel):
    taskSet: ECSTaskSet | None = None
    ResponseMetadata: dict[str, Any] | None = None
