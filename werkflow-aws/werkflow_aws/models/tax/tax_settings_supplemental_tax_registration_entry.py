from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .tax_settings_address import TaxSettingsAddress


class TaxSettingsSupplementalTaxRegistrationEntry(BaseModel):
    registrationId: StrictStr
    registrationType: Literal['VAT']
    legalName: StrictStr
    address: TaxSettingsAddress
