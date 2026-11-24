from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .tax_settings_tax_registration_document import TaxSettingsTaxRegistrationDocument


class TaxSettingsVerificationDetails(BaseModel):
    dateOfBirth: StrictStr | None = None
    taxRegistrationDocuments: list[TaxSettingsTaxRegistrationDocument] | None = None
