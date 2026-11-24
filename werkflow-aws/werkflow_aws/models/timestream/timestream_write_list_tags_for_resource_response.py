from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .timestream_write_tag import TimestreamWriteTag


class TimestreamWriteListTagsForResourceResponse(BaseModel):
    Tags: list[TimestreamWriteTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
