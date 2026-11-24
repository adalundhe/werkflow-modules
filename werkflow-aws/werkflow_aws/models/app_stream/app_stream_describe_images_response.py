from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_stream_image import AppStreamImage


class AppStreamDescribeImagesResponse(BaseModel):
    Images: list[AppStreamImage] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
