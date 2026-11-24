from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineStopExecutionTrigger(BaseModel):
    reason: StrictStr | None = None
