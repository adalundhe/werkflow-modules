from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .cloud_front_encryption_entities import CloudFrontEncryptionEntities


class CloudFrontFieldLevelEncryptionProfileSummary(BaseModel):
    Id: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    Name: StrictStr | None = None
    EncryptionEntities: CloudFrontEncryptionEntities | None = None
    Comment: StrictStr | None = None
