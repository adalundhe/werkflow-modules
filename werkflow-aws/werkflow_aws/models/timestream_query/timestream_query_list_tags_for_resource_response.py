from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .timestream_query_tag import TimestreamQueryTag


class TimestreamQueryListTagsForResourceResponse(BaseModel):
    Tags: list[TimestreamQueryTag] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
