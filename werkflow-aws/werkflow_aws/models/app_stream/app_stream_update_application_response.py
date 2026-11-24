from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .app_stream_application import AppStreamApplication


class AppStreamUpdateApplicationResponse(BaseModel):
    Application: AppStreamApplication | None = None
    ResponseMetadata: dict[str, Any] | None = None
