from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CodePipelineOverrideStageConditionRequest(BaseModel):
    pipelineName: StrictStr
    stageName: StrictStr
    pipelineExecutionId: StrictStr
    conditionType: Literal['BEFORE_ENTRY', 'ON_SUCCESS']
