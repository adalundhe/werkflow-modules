from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelinePipelineRollbackMetadata(BaseModel):
    rollbackTargetPipelineExecutionId: StrictStr | None = None
