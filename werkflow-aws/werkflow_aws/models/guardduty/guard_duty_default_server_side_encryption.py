from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyDefaultServerSideEncryption(BaseModel):
    EncryptionType: StrictStr | None = None
    KmsMasterKeyArn: StrictStr | None = None
