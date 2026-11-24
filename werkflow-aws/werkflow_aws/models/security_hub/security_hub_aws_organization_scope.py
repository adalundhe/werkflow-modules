from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsOrganizationScope(BaseModel):
    OrganizationId: StrictStr | None = None
    OrganizationalUnitId: StrictStr | None = None
