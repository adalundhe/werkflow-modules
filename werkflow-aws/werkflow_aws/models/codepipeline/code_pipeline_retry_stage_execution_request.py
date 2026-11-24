from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CodePipelineRetryStageExecutionRequest(BaseModel):
    pipelineName: StrictStr
    stageName: StrictStr
    pipelineExecutionId: StrictStr
    retryMode: Literal['FAILED_ACTIONS', 'ALL_ACTIONS']
