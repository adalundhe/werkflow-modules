from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CodePipelineStopPipelineExecutionRequest(BaseModel):
    pipelineName: StrictStr
    pipelineExecutionId: StrictStr
    abandon: StrictBool | None = None
    reason: StrictStr | None = None
