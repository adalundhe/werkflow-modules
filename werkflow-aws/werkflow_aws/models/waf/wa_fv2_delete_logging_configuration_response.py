from __future__ import annotations
from typing import Any
from pydantic import BaseModel


class WAFv2DeleteLoggingConfigurationResponse(BaseModel):
    ResponseMetadata: dict[str, Any] | None = None
