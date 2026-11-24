from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_stream_image_builder import AppStreamImageBuilder


class AppStreamDescribeImageBuildersResponse(BaseModel):
    ImageBuilders: list[AppStreamImageBuilder] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
