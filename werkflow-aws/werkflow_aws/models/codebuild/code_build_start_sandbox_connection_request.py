from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildStartSandboxConnectionRequest(BaseModel):
    sandboxId: StrictStr
