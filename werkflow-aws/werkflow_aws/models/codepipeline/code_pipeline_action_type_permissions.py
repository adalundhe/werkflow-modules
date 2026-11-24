from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineActionTypePermissions(BaseModel):
    allowedAccounts: list[StrictStr] | None = None
