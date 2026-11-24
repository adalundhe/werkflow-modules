from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsSecurityFindingIdentifier(BaseModel):
    Id: StrictStr | None = None
    ProductArn: StrictStr | None = None
