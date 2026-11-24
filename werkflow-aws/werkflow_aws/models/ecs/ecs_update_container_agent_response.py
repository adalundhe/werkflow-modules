from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecs_container_instance import ECSContainerInstance


class ECSUpdateContainerAgentResponse(BaseModel):
    containerInstance: ECSContainerInstance | None = None
    ResponseMetadata: dict[str, Any] | None = None
