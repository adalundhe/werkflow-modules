from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .tax_settings_tax_registration_entry import TaxSettingsTaxRegistrationEntry


class TaxSettingsPutTaxRegistrationRequest(BaseModel):
    taxRegistrationEntry: TaxSettingsTaxRegistrationEntry
    accountId: StrictStr | None = None
