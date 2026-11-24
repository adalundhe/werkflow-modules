from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2GetWebACLForResourceRequest(BaseModel):
    ResourceArn: StrictStr
