from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsIamPermissionsBoundary(BaseModel):
    PermissionsBoundaryArn: StrictStr | None = None
    PermissionsBoundaryType: StrictStr | None = None
