from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribePipelineExecutionRequest(BaseModel):
    PipelineExecutionArn: StrictStr
