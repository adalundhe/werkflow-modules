from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .tax_settings_batch_put_tax_registration_error import TaxSettingsBatchPutTaxRegistrationError


class TaxSettingsBatchPutTaxRegistrationResponse(BaseModel):
    status: StrictStr | None = None
    errors: list[TaxSettingsBatchPutTaxRegistrationError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
