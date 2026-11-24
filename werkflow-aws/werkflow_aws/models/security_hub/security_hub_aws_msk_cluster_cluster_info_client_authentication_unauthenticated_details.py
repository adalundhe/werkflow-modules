from __future__ import annotations
from pydantic import BaseModel, StrictBool


class SecurityHubAwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetails(BaseModel):
    Enabled: StrictBool | None = None
