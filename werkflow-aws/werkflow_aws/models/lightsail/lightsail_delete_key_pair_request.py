from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailDeleteKeyPairRequest(BaseModel):
    keyPairName: StrictStr
    expectedFingerprint: StrictStr | None = None
