from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class SSMLabelParameterVersionResponse(BaseModel):
    InvalidLabels: list[StrictStr] | None = None
    ParameterVersion: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
