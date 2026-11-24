from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildRetryBuildRequest(BaseModel):
    id: StrictStr | None = None
    idempotencyToken: StrictStr | None = None
