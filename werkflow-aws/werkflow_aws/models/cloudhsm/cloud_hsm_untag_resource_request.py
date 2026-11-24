from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudHSMUntagResourceRequest(BaseModel):
    ResourceId: StrictStr
    TagKeyList: list[StrictStr]
