from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTKeyPair(BaseModel):
    PublicKey: StrictStr | None = None
    PrivateKey: StrictStr | None = None
