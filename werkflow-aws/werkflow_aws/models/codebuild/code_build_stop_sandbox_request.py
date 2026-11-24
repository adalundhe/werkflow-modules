from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildStopSandboxRequest(BaseModel):
    id: StrictStr
