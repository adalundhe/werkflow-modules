from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecs_failure import ECSFailure
from .ecs_task import ECSTask


class ECSRunTaskResponse(BaseModel):
    tasks: list[ECSTask] | None = None
    failures: list[ECSFailure] | None = None
    ResponseMetadata: dict[str, Any] | None = None
