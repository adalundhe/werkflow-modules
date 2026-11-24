from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .tax_settings_authority import TaxSettingsAuthority


class TaxSettingsTaxExemptionType(BaseModel):
    displayName: StrictStr | None = None
    description: StrictStr | None = None
    applicableJurisdictions: list[TaxSettingsAuthority] | None = None
