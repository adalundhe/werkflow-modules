from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_key_pair import IoTKeyPair


class IoTCreateKeysAndCertificateResponse(BaseModel):
    certificateArn: StrictStr | None = None
    certificateId: StrictStr | None = None
    certificatePem: StrictStr | None = None
    keyPair: IoTKeyPair | None = None
    ResponseMetadata: dict[str, Any] | None = None
