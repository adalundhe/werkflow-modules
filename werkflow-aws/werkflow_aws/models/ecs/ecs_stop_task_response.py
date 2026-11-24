from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecs_task import ECSTask


class ECSStopTaskResponse(BaseModel):
    task: ECSTask | None = None
    ResponseMetadata: dict[str, Any] | None = None
