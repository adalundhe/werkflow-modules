from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_stream_app_block import AppStreamAppBlock


class AppStreamDescribeAppBlocksResponse(BaseModel):
    AppBlocks: list[AppStreamAppBlock] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
