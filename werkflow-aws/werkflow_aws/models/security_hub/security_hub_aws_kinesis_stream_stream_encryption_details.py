from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsKinesisStreamStreamEncryptionDetails(BaseModel):
    EncryptionType: StrictStr | None = None
    KeyId: StrictStr | None = None
