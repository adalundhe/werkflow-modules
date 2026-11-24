from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2IpamScopeExternalAuthorityConfiguration(BaseModel):
    Type: StrictStr | None = None
    ExternalResourceIdentifier: StrictStr | None = None
