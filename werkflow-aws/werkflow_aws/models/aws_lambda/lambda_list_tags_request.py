from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaListTagsRequest(BaseModel):
    Resource: StrictStr
