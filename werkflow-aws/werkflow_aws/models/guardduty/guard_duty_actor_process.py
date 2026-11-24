from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyActorProcess(BaseModel):
    Name: StrictStr | None = None
    Path: StrictStr | None = None
    Sha256: StrictStr | None = None
