from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .tax_settings_tax_exemption import TaxSettingsTaxExemption


class TaxSettingsTaxExemptionDetails(BaseModel):
    taxExemptions: list[TaxSettingsTaxExemption] | None = None
    heritageObtainedDetails: StrictBool | None = None
    heritageObtainedParentEntity: StrictStr | None = None
    heritageObtainedReason: StrictStr | None = None
