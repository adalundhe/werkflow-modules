from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_tag_set import ConnectTagSet


class ConnectSearchResourceTagsResponse(BaseModel):
    Tags: list[ConnectTagSet] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
