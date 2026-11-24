from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerStartPipelineExecutionResponse(BaseModel):
    PipelineExecutionArn: StrictStr | None = None
