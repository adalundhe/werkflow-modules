from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKPublicAccess(BaseModel):
    Type: StrictStr | None = None
