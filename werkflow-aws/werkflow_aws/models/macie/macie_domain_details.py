from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieDomainDetails(BaseModel):
    domainName: StrictStr | None = None
