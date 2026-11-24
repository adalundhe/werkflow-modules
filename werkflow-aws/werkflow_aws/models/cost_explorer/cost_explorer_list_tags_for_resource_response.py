from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cost_explorer_resource_tag import CostExplorerResourceTag


class CostExplorerListTagsForResourceResponse(BaseModel):
    ResourceTags: list[CostExplorerResourceTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
