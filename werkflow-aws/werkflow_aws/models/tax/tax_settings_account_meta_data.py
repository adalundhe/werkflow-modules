from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .tax_settings_address import TaxSettingsAddress
from .tax_settings_jurisdiction import TaxSettingsJurisdiction


class TaxSettingsAccountMetaData(BaseModel):
    accountName: StrictStr | None = None
    seller: StrictStr | None = None
    address: TaxSettingsAddress | None = None
    addressType: StrictStr | None = None
    addressRoleMap: dict[StrictStr, TaxSettingsJurisdiction] | None = None
