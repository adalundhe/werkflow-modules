from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsSaudiArabiaAdditionalInfo(BaseModel):
    taxRegistrationNumberType: StrictStr | None = None
