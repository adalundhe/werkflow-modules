from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .io_t_registration_config import IoTRegistrationConfig


class IoTUpdateCACertificateRequest(BaseModel):
    certificateId: StrictStr
    newStatus: Literal['ACTIVE', 'INACTIVE'] | None = None
    newAutoRegistrationStatus: Literal['ENABLE', 'DISABLE'] | None = None
    registrationConfig: IoTRegistrationConfig | None = None
    removeAutoRegistration: StrictBool | None = None
