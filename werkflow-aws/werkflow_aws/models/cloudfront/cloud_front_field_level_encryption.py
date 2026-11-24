from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .cloud_front_field_level_encryption_config import CloudFrontFieldLevelEncryptionConfig


class CloudFrontFieldLevelEncryption(BaseModel):
    Id: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    FieldLevelEncryptionConfig: CloudFrontFieldLevelEncryptionConfig | None = None
