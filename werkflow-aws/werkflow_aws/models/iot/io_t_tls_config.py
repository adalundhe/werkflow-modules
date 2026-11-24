from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTTlsConfig(BaseModel):
    securityPolicy: StrictStr | None = None
