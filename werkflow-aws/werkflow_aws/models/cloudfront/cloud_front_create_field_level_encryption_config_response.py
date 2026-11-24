from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_front_field_level_encryption import CloudFrontFieldLevelEncryption


class CloudFrontCreateFieldLevelEncryptionConfigResponse(BaseModel):
    FieldLevelEncryption: CloudFrontFieldLevelEncryption | None = None
    Location: StrictStr | None = None
    ETag: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
