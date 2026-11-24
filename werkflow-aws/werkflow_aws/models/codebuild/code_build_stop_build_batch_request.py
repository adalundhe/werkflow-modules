from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildStopBuildBatchRequest(BaseModel):
    id: StrictStr
