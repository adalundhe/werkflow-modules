from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecs_service import ECSService


class ECSDeleteServiceResponse(BaseModel):
    service: ECSService | None = None
    ResponseMetadata: dict[str, Any] | None = None
