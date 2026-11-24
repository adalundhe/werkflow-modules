from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectSecurityProfileSearchSummary(BaseModel):
    Id: StrictStr | None = None
    OrganizationResourceId: StrictStr | None = None
    Arn: StrictStr | None = None
    SecurityProfileName: StrictStr | None = None
    Description: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    Type: StrictStr | None = None
