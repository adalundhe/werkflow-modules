from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .tax_settings_tax_exemption_details import TaxSettingsTaxExemptionDetails


class TaxSettingsListTaxExemptionsResponse(BaseModel):
    nextToken: StrictStr | None = None
    taxExemptionDetailsMap: dict[StrictStr, TaxSettingsTaxExemptionDetails] | None = None
    ResponseMetadata: dict[str, Any] | None = None
