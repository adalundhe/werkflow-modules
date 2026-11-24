from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool


class EC2DisableSerialConsoleAccessResponse(BaseModel):
    SerialConsoleAccessEnabled: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
