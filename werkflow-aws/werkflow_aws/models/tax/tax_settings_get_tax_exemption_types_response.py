from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .tax_settings_tax_exemption_type import TaxSettingsTaxExemptionType


class TaxSettingsGetTaxExemptionTypesResponse(BaseModel):
    taxExemptionTypes: list[TaxSettingsTaxExemptionType] | None = None
    ResponseMetadata: dict[str, Any] | None = None
