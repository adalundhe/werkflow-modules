from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsMalaysiaAdditionalInfo(BaseModel):
    serviceTaxCodes: list[StrictStr] | None = None
    taxInformationNumber: StrictStr | None = None
    businessRegistrationNumber: StrictStr | None = None
