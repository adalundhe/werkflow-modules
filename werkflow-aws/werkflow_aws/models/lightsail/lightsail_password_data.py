from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailPasswordData(BaseModel):
    ciphertext: StrictStr | None = None
    keyPairName: StrictStr | None = None
