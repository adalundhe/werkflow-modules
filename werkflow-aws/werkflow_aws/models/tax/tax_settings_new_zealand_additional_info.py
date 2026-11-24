from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsNewZealandAdditionalInfo(BaseModel):
    peppolId: StrictStr | None = None
