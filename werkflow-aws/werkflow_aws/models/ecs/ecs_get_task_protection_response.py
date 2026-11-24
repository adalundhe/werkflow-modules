from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecs_failure import ECSFailure
from .ecs_protected_task import ECSProtectedTask


class ECSGetTaskProtectionResponse(BaseModel):
    protectedTasks: list[ECSProtectedTask] | None = None
    failures: list[ECSFailure] | None = None
    ResponseMetadata: dict[str, Any] | None = None
