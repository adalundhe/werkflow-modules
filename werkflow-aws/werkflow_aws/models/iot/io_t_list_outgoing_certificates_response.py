from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_outgoing_certificate import IoTOutgoingCertificate


class IoTListOutgoingCertificatesResponse(BaseModel):
    outgoingCertificates: list[IoTOutgoingCertificate] | None = None
    nextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
