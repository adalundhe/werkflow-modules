from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildFleetStatus(BaseModel):
    statusCode: StrictStr | None = None
    context: StrictStr | None = None
    message: StrictStr | None = None
