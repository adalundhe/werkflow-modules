from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_certificate import IoTCertificate


class IoTListCertificatesResponse(BaseModel):
    certificates: list[IoTCertificate] | None = None
    nextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
