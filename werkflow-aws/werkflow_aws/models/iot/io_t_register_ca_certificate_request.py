from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .io_t_registration_config import IoTRegistrationConfig
from .io_t_tag import IoTTag


class IoTRegisterCACertificateRequest(BaseModel):
    caCertificate: StrictStr
    verificationCertificate: StrictStr | None = None
    setAsActive: StrictBool | None = None
    allowAutoRegistration: StrictBool | None = None
    registrationConfig: IoTRegistrationConfig | None = None
    tags: list[IoTTag] | None = None
    certificateMode: Literal['DEFAULT', 'SNI_ONLY'] | None = None
