from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyKeyObservations(BaseModel):
    Title: StrictStr | None = None
    Narrative: StrictStr | None = None
    Observations: list[StrictStr] | None = None
