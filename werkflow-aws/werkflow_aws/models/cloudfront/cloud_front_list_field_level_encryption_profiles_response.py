from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_front_field_level_encryption_profile_list import CloudFrontFieldLevelEncryptionProfileList


class CloudFrontListFieldLevelEncryptionProfilesResponse(BaseModel):
    FieldLevelEncryptionProfileList: CloudFrontFieldLevelEncryptionProfileList | None = None
    ResponseMetadata: dict[str, Any] | None = None
