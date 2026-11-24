from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2FederatedAuthentication(BaseModel):
    SamlProviderArn: StrictStr | None = None
    SelfServiceSamlProviderArn: StrictStr | None = None
