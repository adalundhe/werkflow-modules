from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineStageConditionsExecution(BaseModel):
    status: StrictStr | None = None
    summary: StrictStr | None = None
