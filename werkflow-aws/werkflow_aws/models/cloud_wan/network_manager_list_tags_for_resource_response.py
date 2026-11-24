from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .network_manager_tag import NetworkManagerTag


class NetworkManagerListTagsForResourceResponse(BaseModel):
    TagList: list[NetworkManagerTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
