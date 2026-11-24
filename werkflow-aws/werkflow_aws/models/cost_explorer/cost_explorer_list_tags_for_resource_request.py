from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CostExplorerListTagsForResourceRequest(BaseModel):
    ResourceArn: StrictStr
