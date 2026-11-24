from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .tax_settings_supplemental_tax_registration import TaxSettingsSupplementalTaxRegistration


class TaxSettingsListSupplementalTaxRegistrationsResponse(BaseModel):
    taxRegistrations: list[TaxSettingsSupplementalTaxRegistration] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
