from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ProjectRoleUser(BaseModel):
    accountId: StrictStr | None = None
