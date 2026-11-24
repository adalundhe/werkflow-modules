from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .tax_settings_tax_registration import TaxSettingsTaxRegistration


class TaxSettingsGetTaxRegistrationResponse(BaseModel):
    taxRegistration: TaxSettingsTaxRegistration | None = None
    ResponseMetadata: dict[str, Any] | None = None
