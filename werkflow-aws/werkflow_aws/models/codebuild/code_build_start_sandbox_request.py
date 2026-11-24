from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildStartSandboxRequest(BaseModel):
    projectName: StrictStr | None = None
    idempotencyToken: StrictStr | None = None
