from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightSmallMultiplesAxisProperties(BaseModel):
    Scale: StrictStr | None = None
    Placement: StrictStr | None = None
