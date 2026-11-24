from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ComprehendStartFlywheelIterationResponse(BaseModel):
    FlywheelArn: StrictStr | None = None
    FlywheelIterationId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
