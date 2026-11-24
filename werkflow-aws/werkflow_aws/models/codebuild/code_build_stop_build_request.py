from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildStopBuildRequest(BaseModel):
    id: StrictStr
