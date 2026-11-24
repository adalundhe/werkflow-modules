from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaUntagResourceRequest(BaseModel):
    Resource: StrictStr
    TagKeys: list[StrictStr]
