from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsTurkeyAdditionalInfo(BaseModel):
    taxOffice: StrictStr | None = None
    kepEmailId: StrictStr | None = None
    secondaryTaxId: StrictStr | None = None
    industries: StrictStr | None = None
