from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .app_stream_fleet import AppStreamFleet


class AppStreamUpdateFleetResponse(BaseModel):
    Fleet: AppStreamFleet | None = None
    ResponseMetadata: dict[str, Any] | None = None
