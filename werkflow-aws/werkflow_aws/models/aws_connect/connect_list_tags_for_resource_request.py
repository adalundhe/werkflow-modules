from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectListTagsForResourceRequest(BaseModel):
    resourceArn: StrictStr
