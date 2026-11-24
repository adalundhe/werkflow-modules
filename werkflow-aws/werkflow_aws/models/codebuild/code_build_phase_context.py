from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildPhaseContext(BaseModel):
    statusCode: StrictStr | None = None
    message: StrictStr | None = None
