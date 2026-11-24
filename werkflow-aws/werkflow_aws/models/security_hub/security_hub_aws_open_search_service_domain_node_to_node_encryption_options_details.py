from __future__ import annotations
from pydantic import BaseModel, StrictBool


class SecurityHubAwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetails(BaseModel):
    Enabled: StrictBool | None = None
