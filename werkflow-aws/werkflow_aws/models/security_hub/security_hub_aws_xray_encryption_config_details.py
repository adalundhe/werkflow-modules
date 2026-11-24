from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsXrayEncryptionConfigDetails(BaseModel):
    KeyId: StrictStr | None = None
    Status: StrictStr | None = None
    Type: StrictStr | None = None
