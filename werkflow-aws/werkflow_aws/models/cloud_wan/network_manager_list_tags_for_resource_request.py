from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerListTagsForResourceRequest(BaseModel):
    ResourceArn: StrictStr
