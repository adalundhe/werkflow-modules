from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DocumentDBDBClusterRole(BaseModel):
    RoleArn: StrictStr | None = None
    Status: StrictStr | None = None
