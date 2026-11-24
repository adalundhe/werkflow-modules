from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRCreateSecurityConfigurationRequest(BaseModel):
    Name: StrictStr
    SecurityConfiguration: StrictStr
