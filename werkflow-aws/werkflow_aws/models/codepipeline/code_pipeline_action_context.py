from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineActionContext(BaseModel):
    name: StrictStr | None = None
    actionExecutionId: StrictStr | None = None
