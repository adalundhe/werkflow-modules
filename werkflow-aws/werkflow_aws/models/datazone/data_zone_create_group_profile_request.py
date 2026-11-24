from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneCreateGroupProfileRequest(BaseModel):
    domainIdentifier: StrictStr
    groupIdentifier: StrictStr | None = None
    rolePrincipalArn: StrictStr | None = None
    clientToken: StrictStr | None = None
