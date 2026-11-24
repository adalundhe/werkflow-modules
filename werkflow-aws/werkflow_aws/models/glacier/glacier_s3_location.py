from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glacier_encryption import GlacierEncryption
from .glacier_grant import GlacierGrant


class GlacierS3Location(BaseModel):
    BucketName: StrictStr | None = None
    Prefix: StrictStr | None = None
    Encryption: GlacierEncryption | None = None
    CannedACL: StrictStr | None = None
    AccessControlList: list[GlacierGrant] | None = None
    Tagging: dict[StrictStr, StrictStr] | None = None
    UserMetadata: dict[StrictStr, StrictStr] | None = None
    StorageClass: StrictStr | None = None
