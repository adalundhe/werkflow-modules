from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SSMDeleteParametersResponse(BaseModel):
    DeletedParameters: list[StrictStr] | None = None
    InvalidParameters: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
