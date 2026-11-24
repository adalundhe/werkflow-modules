from __future__ import annotations
from pydantic import BaseModel, StrictBool


class SecurityHubAwsMskClusterClusterInfoClientAuthenticationSaslIamDetails(BaseModel):
    Enabled: StrictBool | None = None
