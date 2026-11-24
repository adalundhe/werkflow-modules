from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildDockerServerStatus(BaseModel):
    status: StrictStr | None = None
    message: StrictStr | None = None
