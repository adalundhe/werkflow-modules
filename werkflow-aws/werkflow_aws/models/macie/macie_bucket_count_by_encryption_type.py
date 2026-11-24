from __future__ import annotations
from pydantic import BaseModel, StrictInt


class MacieBucketCountByEncryptionType(BaseModel):
    kmsManaged: StrictInt | None = None
    s3Managed: StrictInt | None = None
    unencrypted: StrictInt | None = None
    unknown: StrictInt | None = None
