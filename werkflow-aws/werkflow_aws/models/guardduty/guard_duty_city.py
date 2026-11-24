from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyCity(BaseModel):
    CityName: StrictStr | None = None
