from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDeleteSecurityConfigurationRequest(BaseModel):
    Name: StrictStr
