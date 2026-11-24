from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_security_profile import ConnectSecurityProfile


class ConnectDescribeSecurityProfileResponse(BaseModel):
    SecurityProfile: ConnectSecurityProfile | None = None
    ResponseMetadata: dict[str, Any] | None = None
