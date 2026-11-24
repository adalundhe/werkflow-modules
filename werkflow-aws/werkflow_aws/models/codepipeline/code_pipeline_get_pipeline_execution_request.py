from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineGetPipelineExecutionRequest(BaseModel):
    pipelineName: StrictStr
    pipelineExecutionId: StrictStr
