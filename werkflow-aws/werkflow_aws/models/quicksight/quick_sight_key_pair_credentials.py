from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightKeyPairCredentials(BaseModel):
    KeyPairUsername: StrictStr
    PrivateKey: StrictStr
    PrivateKeyPassphrase: StrictStr | None = None
