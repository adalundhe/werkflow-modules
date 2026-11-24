from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerStopPipelineExecutionRequest(BaseModel):
    PipelineExecutionArn: StrictStr
    ClientRequestToken: StrictStr
