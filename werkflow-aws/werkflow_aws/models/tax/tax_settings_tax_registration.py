from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .tax_settings_additional_info_response import TaxSettingsAdditionalInfoResponse
from .tax_settings_address import TaxSettingsAddress
from .tax_settings_tax_document_metadata import TaxSettingsTaxDocumentMetadata
from .tax_settings_tax_registration_status_reason import TaxSettingsTaxRegistrationStatusReason


class TaxSettingsTaxRegistration(BaseModel):
    registrationId: StrictStr | None = None
    registrationType: StrictStr | None = None
    legalName: StrictStr | None = None
    status: StrictStr | None = None
    sector: StrictStr | None = None
    taxDocumentMetadatas: list[TaxSettingsTaxDocumentMetadata] | None = None
    certifiedEmailId: StrictStr | None = None
    additionalTaxInformation: TaxSettingsAdditionalInfoResponse | None = None
    statusReason: TaxSettingsTaxRegistrationStatusReason | None = None
    legalAddress: TaxSettingsAddress | None = None
