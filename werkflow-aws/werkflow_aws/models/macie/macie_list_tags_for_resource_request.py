from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieListTagsForResourceRequest(BaseModel):
    resourceArn: StrictStr
