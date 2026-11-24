from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsUkraineAdditionalInfo(BaseModel):
    ukraineTrnType: StrictStr | None = None
