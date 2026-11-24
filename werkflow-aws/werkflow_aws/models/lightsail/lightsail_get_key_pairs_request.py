from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LightsailGetKeyPairsRequest(BaseModel):
    pageToken: StrictStr | None = None
    includeDefaultKeyPair: StrictBool | None = None
