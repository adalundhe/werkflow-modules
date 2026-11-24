from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .fis_target_resource_type import FISTargetResourceType


class FISGetTargetResourceTypeResponse(BaseModel):
    targetResourceType: FISTargetResourceType | None = None
    ResponseMetadata: dict[str, Any] | None = None
