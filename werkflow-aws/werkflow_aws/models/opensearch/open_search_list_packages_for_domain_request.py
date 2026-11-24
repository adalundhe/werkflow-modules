from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class OpenSearchListPackagesForDomainRequest(BaseModel):
    DomainName: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
