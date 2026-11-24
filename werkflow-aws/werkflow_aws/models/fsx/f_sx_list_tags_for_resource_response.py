from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .f_sx_tag import FSxTag


class FSxListTagsForResourceResponse(BaseModel):
    Tags: list[FSxTag] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
