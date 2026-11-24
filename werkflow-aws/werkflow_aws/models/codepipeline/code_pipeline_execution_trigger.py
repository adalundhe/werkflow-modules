from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineExecutionTrigger(BaseModel):
    triggerType: StrictStr | None = None
    triggerDetail: StrictStr | None = None
