from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildBuildNotDeleted(BaseModel):
    id: StrictStr | None = None
    statusCode: StrictStr | None = None
