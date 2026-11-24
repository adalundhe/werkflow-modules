from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class IoTRegisterCertificateRequest(BaseModel):
    certificatePem: StrictStr
    caCertificatePem: StrictStr | None = None
    setAsActive: StrictBool | None = None
    status: Literal['ACTIVE', 'INACTIVE', 'REVOKED', 'PENDING_TRANSFER', 'REGISTER_INACTIVE', 'PENDING_ACTIVATION'] | None = None
