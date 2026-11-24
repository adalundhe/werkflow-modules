from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsGermanyAdditionalInfo(BaseModel):
    economicIdentificationNumber: StrictStr | None = None
    steuernummer: StrictStr | None = None
