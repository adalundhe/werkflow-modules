from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .tax_settings_tax_exemption_details import TaxSettingsTaxExemptionDetails


class TaxSettingsBatchGetTaxExemptionsResponse(BaseModel):
    taxExemptionDetailsMap: dict[StrictStr, TaxSettingsTaxExemptionDetails] | None = None
    failedAccounts: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
