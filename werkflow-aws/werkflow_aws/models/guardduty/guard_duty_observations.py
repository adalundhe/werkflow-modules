from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GuardDutyObservations(BaseModel):
    Text: list[StrictStr] | None = None
    Number: list[StrictInt] | None = None
