from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CodePipelineLatestInPipelineExecutionFilter(BaseModel):
    pipelineExecutionId: StrictStr
    startTimeRange: Literal['Latest', 'All']
