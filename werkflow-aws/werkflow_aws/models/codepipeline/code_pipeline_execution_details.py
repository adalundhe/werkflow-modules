from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CodePipelineExecutionDetails(BaseModel):
    summary: StrictStr | None = None
    externalExecutionId: StrictStr | None = None
    percentComplete: StrictInt | None = None
