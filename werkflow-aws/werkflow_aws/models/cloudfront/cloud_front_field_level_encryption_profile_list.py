from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_front_field_level_encryption_profile_summary import CloudFrontFieldLevelEncryptionProfileSummary


class CloudFrontFieldLevelEncryptionProfileList(BaseModel):
    NextMarker: StrictStr | None = None
    MaxItems: StrictInt | None = None
    Quantity: StrictInt | None = None
    Items: list[CloudFrontFieldLevelEncryptionProfileSummary] | None = None
