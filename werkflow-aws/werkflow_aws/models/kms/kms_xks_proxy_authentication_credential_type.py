from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KMSXksProxyAuthenticationCredentialType(BaseModel):
    AccessKeyId: StrictStr
    RawSecretAccessKey: StrictStr
