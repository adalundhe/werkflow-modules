from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_stream_app_block_builder import AppStreamAppBlockBuilder


class AppStreamDescribeAppBlockBuildersResponse(BaseModel):
    AppBlockBuilders: list[AppStreamAppBlockBuilder] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
