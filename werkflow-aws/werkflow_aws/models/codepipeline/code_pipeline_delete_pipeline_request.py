from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineDeletePipelineRequest(BaseModel):
    name: StrictStr
