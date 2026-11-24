from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeGuruTagResourceRequest(BaseModel):
    resourceArn: StrictStr
    Tags: dict[StrictStr, StrictStr]
