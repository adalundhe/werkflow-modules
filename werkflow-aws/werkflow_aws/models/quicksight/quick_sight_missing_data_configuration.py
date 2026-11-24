from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightMissingDataConfiguration(BaseModel):
    TreatmentOption: StrictStr | None = None
