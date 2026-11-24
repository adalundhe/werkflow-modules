from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribePipelineDefinitionForExecutionRequest(BaseModel):
    PipelineExecutionArn: StrictStr
