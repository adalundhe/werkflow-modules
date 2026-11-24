from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsDeleteSupplementalTaxRegistrationRequest(BaseModel):
    authorityId: StrictStr
