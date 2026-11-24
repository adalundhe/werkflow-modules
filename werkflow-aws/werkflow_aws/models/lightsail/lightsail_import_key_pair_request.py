from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailImportKeyPairRequest(BaseModel):
    keyPairName: StrictStr
    publicKeyBase64: StrictStr
