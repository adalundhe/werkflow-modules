from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailGetKeyPairRequest(BaseModel):
    keyPairName: StrictStr
