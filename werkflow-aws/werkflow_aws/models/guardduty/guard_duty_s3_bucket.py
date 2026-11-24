from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .guard_duty_public_access_configuration import GuardDutyPublicAccessConfiguration


class GuardDutyS3Bucket(BaseModel):
    OwnerId: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    EncryptionType: StrictStr | None = None
    EncryptionKeyArn: StrictStr | None = None
    EffectivePermission: StrictStr | None = None
    PublicReadAccess: StrictStr | None = None
    PublicWriteAccess: StrictStr | None = None
    AccountPublicAccess: GuardDutyPublicAccessConfiguration | None = None
    BucketPublicAccess: GuardDutyPublicAccessConfiguration | None = None
    S3ObjectUids: list[StrictStr] | None = None
