from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .tax_settings_tax_registration_entry import TaxSettingsTaxRegistrationEntry


class TaxSettingsBatchPutTaxRegistrationRequest(BaseModel):
    accountIds: list[StrictStr]
    taxRegistrationEntry: TaxSettingsTaxRegistrationEntry
