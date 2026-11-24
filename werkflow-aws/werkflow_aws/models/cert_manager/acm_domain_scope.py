from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ACMDomainScope(BaseModel):
    ExactDomain: StrictStr | None = None
    Subdomains: StrictStr | None = None
    Wildcards: StrictStr | None = None
