from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .tax_settings_authority import TaxSettingsAuthority
from .tax_settings_tax_exemption_type import TaxSettingsTaxExemptionType


class TaxSettingsTaxExemption(BaseModel):
    authority: TaxSettingsAuthority | None = None
    taxExemptionType: TaxSettingsTaxExemptionType | None = None
    effectiveDate: datetime.datetime | StrictStr | None = None
    expirationDate: datetime.datetime | StrictStr | None = None
    systemEffectiveDate: datetime.datetime | StrictStr | None = None
    status: StrictStr | None = None
