from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .app_stream_app_block import AppStreamAppBlock


class AppStreamCreateAppBlockResponse(BaseModel):
    AppBlock: AppStreamAppBlock | None = None
    ResponseMetadata: dict[str, Any] | None = None
