from __future__ import annotations
from pydantic import BaseModel, StrictBool


class SecurityHubAwsMskClusterClusterInfoClientAuthenticationSaslScramDetails(BaseModel):
    Enabled: StrictBool | None = None
