from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_field_patterns import CloudFrontFieldPatterns


class CloudFrontEncryptionEntity(BaseModel):
    PublicKeyId: StrictStr | None = None
    ProviderId: StrictStr | None = None
    FieldPatterns: CloudFrontFieldPatterns | None = None
