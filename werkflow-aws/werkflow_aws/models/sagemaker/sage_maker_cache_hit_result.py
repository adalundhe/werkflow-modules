from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerCacheHitResult(BaseModel):
    SourcePipelineExecutionArn: StrictStr | None = None
