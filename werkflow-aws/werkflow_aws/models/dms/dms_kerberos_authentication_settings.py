from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSKerberosAuthenticationSettings(BaseModel):
    KeyCacheSecretId: StrictStr | None = None
    KeyCacheSecretIamArn: StrictStr | None = None
    Krb5FileContents: StrictStr | None = None
