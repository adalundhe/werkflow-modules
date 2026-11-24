from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineStageExecution(BaseModel):
    pipelineExecutionId: StrictStr | None = None
    status: StrictStr | None = None
    type: StrictStr | None = None
