from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .io_t_auth_result import IoTAuthResult


class IoTTestAuthorizationResponse(BaseModel):
    authResults: list[IoTAuthResult] | None = None
    ResponseMetadata: dict[str, Any] | None = None
