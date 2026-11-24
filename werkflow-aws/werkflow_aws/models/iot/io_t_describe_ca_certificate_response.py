from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .io_tca_certificate_description import IoTCACertificateDescription
from .io_t_registration_config import IoTRegistrationConfig


class IoTDescribeCACertificateResponse(BaseModel):
    certificateDescription: IoTCACertificateDescription | None = None
    registrationConfig: IoTRegistrationConfig | None = None
    ResponseMetadata: dict[str, Any] | None = None
