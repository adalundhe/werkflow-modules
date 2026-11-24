from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .app_stream_image import AppStreamImage


class AppStreamCreateImportedImageResponse(BaseModel):
    Image: AppStreamImage | None = None
    ResponseMetadata: dict[str, Any] | None = None
