from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsRomaniaAdditionalInfo(BaseModel):
    taxRegistrationNumberType: StrictStr | None = None
