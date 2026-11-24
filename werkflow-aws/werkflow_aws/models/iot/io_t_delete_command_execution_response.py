from __future__ import annotations
from typing import Any
from pydantic import BaseModel


class IoTDeleteCommandExecutionResponse(BaseModel):
    ResponseMetadata: dict[str, Any] | None = None
