from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSTargetHealth(BaseModel):
    State: StrictStr | None = None
    Reason: StrictStr | None = None
    Description: StrictStr | None = None
