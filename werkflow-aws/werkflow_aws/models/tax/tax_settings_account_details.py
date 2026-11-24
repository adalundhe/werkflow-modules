from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .tax_settings_account_meta_data import TaxSettingsAccountMetaData
from .tax_settings_tax_inheritance_details import TaxSettingsTaxInheritanceDetails
from .tax_settings_tax_registration_with_jurisdiction import TaxSettingsTaxRegistrationWithJurisdiction


class TaxSettingsAccountDetails(BaseModel):
    accountId: StrictStr | None = None
    taxRegistration: TaxSettingsTaxRegistrationWithJurisdiction | None = None
    taxInheritanceDetails: TaxSettingsTaxInheritanceDetails | None = None
    accountMetaData: TaxSettingsAccountMetaData | None = None
