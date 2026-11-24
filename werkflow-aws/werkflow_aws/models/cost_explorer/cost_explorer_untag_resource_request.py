from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerUntagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    ResourceTagKeys: list[StrictStr]
