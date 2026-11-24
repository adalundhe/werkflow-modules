from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsIdentitySourceDetails(BaseModel):
    clientIds: list[StrictStr] | None = None
    userPoolArn: StrictStr | None = None
    discoveryUrl: StrictStr | None = None
    openIdIssuer: StrictStr | None = None
