from __future__ import annotations
from pydantic import BaseModel
from .tax_settings_source_s3_location import TaxSettingsSourceS3Location
from .tax_settings_tax_registration_doc_file import TaxSettingsTaxRegistrationDocFile


class TaxSettingsTaxRegistrationDocument(BaseModel):
    s3Location: TaxSettingsSourceS3Location | None = None
    file: TaxSettingsTaxRegistrationDocFile | None = None
