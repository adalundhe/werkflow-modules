from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .tax_settings_authority import TaxSettingsAuthority
from .tax_settings_exemption_certificate import TaxSettingsExemptionCertificate


class TaxSettingsPutTaxExemptionRequest(BaseModel):
    accountIds: list[StrictStr]
    authority: TaxSettingsAuthority
    exemptionType: StrictStr
    exemptionCertificate: TaxSettingsExemptionCertificate
