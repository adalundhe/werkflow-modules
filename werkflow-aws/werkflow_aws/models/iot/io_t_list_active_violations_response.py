from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_active_violation import IoTActiveViolation


class IoTListActiveViolationsResponse(BaseModel):
    activeViolations: list[IoTActiveViolation] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
