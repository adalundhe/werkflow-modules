from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_field_level_encryption_config import CloudFrontFieldLevelEncryptionConfig


class CloudFrontUpdateFieldLevelEncryptionConfigRequest(BaseModel):
    FieldLevelEncryptionConfig: CloudFrontFieldLevelEncryptionConfig
    Id: StrictStr
    IfMatch: StrictStr | None = None
