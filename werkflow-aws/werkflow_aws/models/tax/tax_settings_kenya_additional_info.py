from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsKenyaAdditionalInfo(BaseModel):
    personType: StrictStr | None = None
