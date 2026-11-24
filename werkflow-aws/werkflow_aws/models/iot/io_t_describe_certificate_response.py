from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .io_t_certificate_description import IoTCertificateDescription


class IoTDescribeCertificateResponse(BaseModel):
    certificateDescription: IoTCertificateDescription | None = None
    ResponseMetadata: dict[str, Any] | None = None
