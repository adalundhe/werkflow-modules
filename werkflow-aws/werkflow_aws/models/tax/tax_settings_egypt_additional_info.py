from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsEgyptAdditionalInfo(BaseModel):
    uniqueIdentificationNumber: StrictStr | None = None
    uniqueIdentificationNumberExpirationDate: StrictStr | None = None
