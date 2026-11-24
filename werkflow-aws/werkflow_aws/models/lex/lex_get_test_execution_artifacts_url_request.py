from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexGetTestExecutionArtifactsUrlRequest(BaseModel):
    testExecutionId: StrictStr
