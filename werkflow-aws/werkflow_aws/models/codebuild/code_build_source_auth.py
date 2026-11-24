from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildSourceAuth(BaseModel):
    type: StrictStr | None = None
    resource: StrictStr | None = None
