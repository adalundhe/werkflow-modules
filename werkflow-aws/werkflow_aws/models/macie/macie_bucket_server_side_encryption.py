from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieBucketServerSideEncryption(BaseModel):
    kmsMasterKeyId: StrictStr | None = None
    type: StrictStr | None = None
