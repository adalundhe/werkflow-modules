from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .tax_settings_batch_delete_tax_registration_error import TaxSettingsBatchDeleteTaxRegistrationError


class TaxSettingsBatchDeleteTaxRegistrationResponse(BaseModel):
    errors: list[TaxSettingsBatchDeleteTaxRegistrationError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
