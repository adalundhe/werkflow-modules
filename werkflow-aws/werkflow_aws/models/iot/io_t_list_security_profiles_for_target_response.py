from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_security_profile_target_mapping import IoTSecurityProfileTargetMapping


class IoTListSecurityProfilesForTargetResponse(BaseModel):
    securityProfileTargetMappings: list[IoTSecurityProfileTargetMapping] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
