from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ELBv2AdministrativeOverride(BaseModel):
    State: StrictStr | None = None
    Reason: StrictStr | None = None
    Description: StrictStr | None = None
