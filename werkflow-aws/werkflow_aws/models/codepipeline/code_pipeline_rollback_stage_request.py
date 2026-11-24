from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineRollbackStageRequest(BaseModel):
    pipelineName: StrictStr
    stageName: StrictStr
    targetPipelineExecutionId: StrictStr
