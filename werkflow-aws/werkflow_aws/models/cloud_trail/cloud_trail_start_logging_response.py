from __future__ import annotations
from typing import Any
from pydantic import BaseModel


class CloudTrailStartLoggingResponse(BaseModel):
    ResponseMetadata: dict[str, Any] | None = None
