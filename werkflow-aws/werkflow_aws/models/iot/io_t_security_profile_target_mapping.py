from __future__ import annotations
from pydantic import BaseModel
from .io_t_security_profile_identifier import IoTSecurityProfileIdentifier
from .io_t_security_profile_target import IoTSecurityProfileTarget


class IoTSecurityProfileTargetMapping(BaseModel):
    securityProfileIdentifier: IoTSecurityProfileIdentifier | None = None
    target: IoTSecurityProfileTarget | None = None
