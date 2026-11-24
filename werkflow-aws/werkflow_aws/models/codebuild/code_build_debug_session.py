from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CodeBuildDebugSession(BaseModel):
    sessionEnabled: StrictBool | None = None
    sessionTarget: StrictStr | None = None
