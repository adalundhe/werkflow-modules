from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_field_level_encryption_profile_config import CloudFrontFieldLevelEncryptionProfileConfig


class CloudFrontUpdateFieldLevelEncryptionProfileRequest(BaseModel):
    FieldLevelEncryptionProfileConfig: CloudFrontFieldLevelEncryptionProfileConfig
    Id: StrictStr
    IfMatch: StrictStr | None = None
