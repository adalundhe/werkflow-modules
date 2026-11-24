from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKUserIdentity(BaseModel):
    Type: StrictStr | None = None
    PrincipalId: StrictStr | None = None
