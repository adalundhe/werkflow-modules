from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_encryption_entities import CloudFrontEncryptionEntities


class CloudFrontFieldLevelEncryptionProfileConfig(BaseModel):
    Name: StrictStr | None = None
    CallerReference: StrictStr | None = None
    Comment: StrictStr | None = None
    EncryptionEntities: CloudFrontEncryptionEntities | None = None
