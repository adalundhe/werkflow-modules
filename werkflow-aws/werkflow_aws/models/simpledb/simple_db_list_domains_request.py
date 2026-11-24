from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SimpleDBListDomainsRequest(BaseModel):
    MaxNumberOfDomains: StrictInt | None = None
    NextToken: StrictStr | None = None
