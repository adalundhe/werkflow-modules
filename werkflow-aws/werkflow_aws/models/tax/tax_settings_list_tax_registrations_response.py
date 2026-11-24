from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .tax_settings_account_details import TaxSettingsAccountDetails


class TaxSettingsListTaxRegistrationsResponse(BaseModel):
    accountDetails: list[TaxSettingsAccountDetails] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
