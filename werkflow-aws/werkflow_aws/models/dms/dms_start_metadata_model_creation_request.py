from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dms_metadata_model_properties import DMSMetadataModelProperties


class DMSStartMetadataModelCreationRequest(BaseModel):
    MigrationProjectIdentifier: StrictStr
    SelectionRules: StrictStr
    MetadataModelName: StrictStr
    Properties: DMSMetadataModelProperties
