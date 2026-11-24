from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CodePipelineDisableStageTransitionRequest(BaseModel):
    pipelineName: StrictStr
    stageName: StrictStr
    transitionType: Literal['Inbound', 'Outbound']
    reason: StrictStr
