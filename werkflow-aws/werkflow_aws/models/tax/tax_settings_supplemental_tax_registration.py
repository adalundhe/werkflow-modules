from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .tax_settings_address import TaxSettingsAddress


class TaxSettingsSupplementalTaxRegistration(BaseModel):
    registrationId: StrictStr | None = None
    registrationType: StrictStr | None = None
    legalName: StrictStr | None = None
    address: TaxSettingsAddress | None = None
    authorityId: StrictStr | None = None
    status: StrictStr | None = None
