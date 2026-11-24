from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class IoTRegisterCertificateWithoutCARequest(BaseModel):
    certificatePem: StrictStr
    status: Literal['ACTIVE', 'INACTIVE', 'REVOKED', 'PENDING_TRANSFER', 'REGISTER_INACTIVE', 'PENDING_ACTIVATION'] | None = None
