from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .cloud_front_field_level_encryption_profile_config import CloudFrontFieldLevelEncryptionProfileConfig


class CloudFrontFieldLevelEncryptionProfile(BaseModel):
    Id: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    FieldLevelEncryptionProfileConfig: CloudFrontFieldLevelEncryptionProfileConfig | None = None
