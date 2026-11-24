from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_front_field_level_encryption_profile_config import CloudFrontFieldLevelEncryptionProfileConfig


class CloudFrontGetFieldLevelEncryptionProfileConfigResponse(BaseModel):
    FieldLevelEncryptionProfileConfig: CloudFrontFieldLevelEncryptionProfileConfig | None = None
    ETag: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
