from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GuardDutyAutonomousSystem(BaseModel):
    Name: StrictStr | None = None
    Number: StrictInt | None = None
