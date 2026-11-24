from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lightsail_key_pair import LightsailKeyPair


class LightsailGetKeyPairsResponse(BaseModel):
    keyPairs: list[LightsailKeyPair] | None = None
    nextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
