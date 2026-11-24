from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_tca_certificate import IoTCACertificate


class IoTListCACertificatesResponse(BaseModel):
    certificates: list[IoTCACertificate] | None = None
    nextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
