from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTUpdateDeviceCertificateParams(BaseModel):
    action: StrictStr | None = None
