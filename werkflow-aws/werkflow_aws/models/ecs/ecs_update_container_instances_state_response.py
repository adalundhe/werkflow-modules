from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecs_container_instance import ECSContainerInstance
from .ecs_failure import ECSFailure


class ECSUpdateContainerInstancesStateResponse(BaseModel):
    containerInstances: list[ECSContainerInstance] | None = None
    failures: list[ECSFailure] | None = None
    ResponseMetadata: dict[str, Any] | None = None
