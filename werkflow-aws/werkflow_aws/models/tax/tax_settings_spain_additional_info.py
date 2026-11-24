from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsSpainAdditionalInfo(BaseModel):
    registrationType: StrictStr | None = None
