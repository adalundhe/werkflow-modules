from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildBuildStatusConfig(BaseModel):
    context: StrictStr | None = None
    targetUrl: StrictStr | None = None
