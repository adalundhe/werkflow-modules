from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsIndonesiaAdditionalInfo(BaseModel):
    taxRegistrationNumberType: StrictStr | None = None
    ppnExceptionDesignationCode: StrictStr | None = None
    decisionNumber: StrictStr | None = None
