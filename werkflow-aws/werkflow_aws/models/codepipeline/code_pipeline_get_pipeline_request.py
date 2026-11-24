from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CodePipelineGetPipelineRequest(BaseModel):
    name: StrictStr
    version: StrictInt | None = None
