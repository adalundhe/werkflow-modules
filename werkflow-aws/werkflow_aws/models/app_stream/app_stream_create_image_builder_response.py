from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .app_stream_image_builder import AppStreamImageBuilder


class AppStreamCreateImageBuilderResponse(BaseModel):
    ImageBuilder: AppStreamImageBuilder | None = None
    ResponseMetadata: dict[str, Any] | None = None
