from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .direct_connect_resource_tag import DirectConnectResourceTag


class DirectConnectDescribeTagsResponse(BaseModel):
    resourceTags: list[DirectConnectResourceTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
