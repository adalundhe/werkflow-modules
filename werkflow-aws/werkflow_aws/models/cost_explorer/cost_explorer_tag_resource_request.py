from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cost_explorer_resource_tag import CostExplorerResourceTag


class CostExplorerTagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    ResourceTags: list[CostExplorerResourceTag]
