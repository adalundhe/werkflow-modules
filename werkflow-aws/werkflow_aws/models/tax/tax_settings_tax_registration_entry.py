from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .tax_settings_additional_info_request import TaxSettingsAdditionalInfoRequest
from .tax_settings_address import TaxSettingsAddress
from .tax_settings_verification_details import TaxSettingsVerificationDetails


class TaxSettingsTaxRegistrationEntry(BaseModel):
    registrationId: StrictStr
    registrationType: Literal['VAT', 'GST', 'CPF', 'CNPJ', 'SST', 'TIN', 'NRIC', 'PAN', 'NIP', 'CUIT', 'CDI', 'RUT', 'NIE', 'CI']
    legalName: StrictStr | None = None
    legalAddress: TaxSettingsAddress | None = None
    sector: Literal['Business', 'Individual', 'Government'] | None = None
    additionalTaxInformation: TaxSettingsAdditionalInfoRequest | None = None
    verificationDetails: TaxSettingsVerificationDetails | None = None
    certifiedEmailId: StrictStr | None = None
