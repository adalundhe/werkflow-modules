from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SecurityLakeCreateAwsLogSourceResponse(BaseModel):
    failed: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
