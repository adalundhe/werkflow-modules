from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAwsRedshiftClusterEndpoint(BaseModel):
    Address: StrictStr | None = None
    Port: StrictInt | None = None
