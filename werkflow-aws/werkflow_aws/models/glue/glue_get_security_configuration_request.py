from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetSecurityConfigurationRequest(BaseModel):
    Name: StrictStr
