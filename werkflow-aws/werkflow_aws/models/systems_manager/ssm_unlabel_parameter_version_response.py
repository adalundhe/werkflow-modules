from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SSMUnlabelParameterVersionResponse(BaseModel):
    RemovedLabels: list[StrictStr] | None = None
    InvalidLabels: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
