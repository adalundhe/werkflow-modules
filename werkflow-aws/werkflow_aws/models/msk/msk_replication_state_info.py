from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKReplicationStateInfo(BaseModel):
    Code: StrictStr | None = None
    Message: StrictStr | None = None
