from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_front_field_level_encryption_summary import CloudFrontFieldLevelEncryptionSummary


class CloudFrontFieldLevelEncryptionList(BaseModel):
    NextMarker: StrictStr | None = None
    MaxItems: StrictInt | None = None
    Quantity: StrictInt | None = None
    Items: list[CloudFrontFieldLevelEncryptionSummary] | None = None
