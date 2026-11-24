from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lightsail_key_pair import LightsailKeyPair
from .lightsail_operation import LightsailOperation


class LightsailCreateKeyPairResponse(BaseModel):
    keyPair: LightsailKeyPair | None = None
    publicKeyBase64: StrictStr | None = None
    privateKeyBase64: StrictStr | None = None
    operation: LightsailOperation | None = None
    ResponseMetadata: dict[str, Any] | None = None
