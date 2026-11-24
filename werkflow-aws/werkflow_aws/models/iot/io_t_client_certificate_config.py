from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTClientCertificateConfig(BaseModel):
    clientCertificateCallbackArn: StrictStr | None = None
