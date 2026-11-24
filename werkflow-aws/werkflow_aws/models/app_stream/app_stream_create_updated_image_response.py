from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool
from .app_stream_image import AppStreamImage


class AppStreamCreateUpdatedImageResponse(BaseModel):
    image: AppStreamImage | None = None
    canUpdateImage: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
