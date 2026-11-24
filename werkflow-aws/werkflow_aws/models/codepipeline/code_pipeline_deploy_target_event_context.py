from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineDeployTargetEventContext(BaseModel):
    ssmCommandId: StrictStr | None = None
    message: StrictStr | None = None
