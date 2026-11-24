from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKReplicationStartingPosition(BaseModel):
    Type: StrictStr | None = None
