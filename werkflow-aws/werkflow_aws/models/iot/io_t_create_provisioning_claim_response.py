from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_key_pair import IoTKeyPair


class IoTCreateProvisioningClaimResponse(BaseModel):
    certificateId: StrictStr | None = None
    certificatePem: StrictStr | None = None
    keyPair: IoTKeyPair | None = None
    expiration: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
