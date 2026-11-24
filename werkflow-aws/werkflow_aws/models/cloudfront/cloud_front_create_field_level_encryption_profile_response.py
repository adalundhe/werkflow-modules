from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_front_field_level_encryption_profile import CloudFrontFieldLevelEncryptionProfile


class CloudFrontCreateFieldLevelEncryptionProfileResponse(BaseModel):
    FieldLevelEncryptionProfile: CloudFrontFieldLevelEncryptionProfile | None = None
    Location: StrictStr | None = None
    ETag: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
