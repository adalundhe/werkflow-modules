from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildScopeConfiguration(BaseModel):
    name: StrictStr | None = None
    domain: StrictStr | None = None
    scope: StrictStr | None = None
