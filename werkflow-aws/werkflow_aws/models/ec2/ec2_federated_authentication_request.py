from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2FederatedAuthenticationRequest(BaseModel):
    SAMLProviderArn: StrictStr | None = None
    SelfServiceSAMLProviderArn: StrictStr | None = None
