from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lightsail_operation import LightsailOperation


class LightsailDeleteDomainResponse(BaseModel):
    operation: LightsailOperation | None = None
    ResponseMetadata: dict[str, Any] | None = None
