from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsUnitedArabEmiratesAdditionalInfo(BaseModel):
    taxRegistrationNumberType: StrictStr | None = None
    peppolId: StrictStr | None = None
    tradeLicenseNumber: StrictStr | None = None
    emiratesId: StrictStr | None = None
