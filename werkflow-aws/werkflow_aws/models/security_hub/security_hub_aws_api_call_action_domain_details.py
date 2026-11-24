from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsApiCallActionDomainDetails(BaseModel):
    Domain: StrictStr | None = None
