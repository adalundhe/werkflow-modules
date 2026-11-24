from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsUzbekistanAdditionalInfo(BaseModel):
    taxRegistrationNumberType: StrictStr | None = None
    vatRegistrationNumber: StrictStr | None = None
