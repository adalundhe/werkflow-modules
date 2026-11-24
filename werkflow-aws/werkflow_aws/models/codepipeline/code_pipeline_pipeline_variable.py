from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelinePipelineVariable(BaseModel):
    name: StrictStr
    value: StrictStr
