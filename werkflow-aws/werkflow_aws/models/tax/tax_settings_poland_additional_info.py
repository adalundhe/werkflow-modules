from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class TaxSettingsPolandAdditionalInfo(BaseModel):
    individualRegistrationNumber: StrictStr | None = None
    isGroupVatEnabled: StrictBool | None = None
    taxRegistrationNumberType: StrictStr | None = None
