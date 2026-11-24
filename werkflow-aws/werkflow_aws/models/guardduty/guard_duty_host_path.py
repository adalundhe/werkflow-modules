from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyHostPath(BaseModel):
    Path: StrictStr | None = None
