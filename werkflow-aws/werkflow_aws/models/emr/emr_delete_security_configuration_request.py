from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRDeleteSecurityConfigurationRequest(BaseModel):
    Name: StrictStr
