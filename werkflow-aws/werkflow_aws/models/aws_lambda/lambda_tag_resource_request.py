from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaTagResourceRequest(BaseModel):
    Resource: StrictStr
    Tags: dict[StrictStr, StrictStr]
