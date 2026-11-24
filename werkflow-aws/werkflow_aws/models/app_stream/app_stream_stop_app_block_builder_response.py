from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .app_stream_app_block_builder import AppStreamAppBlockBuilder


class AppStreamStopAppBlockBuilderResponse(BaseModel):
    AppBlockBuilder: AppStreamAppBlockBuilder | None = None
    ResponseMetadata: dict[str, Any] | None = None
