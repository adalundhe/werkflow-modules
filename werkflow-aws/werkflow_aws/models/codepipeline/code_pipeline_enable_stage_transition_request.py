from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CodePipelineEnableStageTransitionRequest(BaseModel):
    pipelineName: StrictStr
    stageName: StrictStr
    transitionType: Literal['Inbound', 'Outbound']
