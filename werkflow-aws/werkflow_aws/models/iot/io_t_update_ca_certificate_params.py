from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTUpdateCACertificateParams(BaseModel):
    action: StrictStr | None = None
