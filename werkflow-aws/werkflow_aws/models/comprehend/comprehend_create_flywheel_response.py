from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ComprehendCreateFlywheelResponse(BaseModel):
    FlywheelArn: StrictStr | None = None
    ActiveModelArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
