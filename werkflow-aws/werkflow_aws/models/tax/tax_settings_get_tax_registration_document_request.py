from __future__ import annotations
from pydantic import BaseModel
from .tax_settings_destination_s3_location import TaxSettingsDestinationS3Location
from .tax_settings_tax_document_metadata import TaxSettingsTaxDocumentMetadata


class TaxSettingsGetTaxRegistrationDocumentRequest(BaseModel):
    taxDocumentMetadata: TaxSettingsTaxDocumentMetadata
    destinationS3Location: TaxSettingsDestinationS3Location | None = None
