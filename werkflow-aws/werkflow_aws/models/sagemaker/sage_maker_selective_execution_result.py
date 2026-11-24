from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerSelectiveExecutionResult(BaseModel):
    SourcePipelineExecutionArn: StrictStr | None = None
