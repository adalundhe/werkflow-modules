from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchListVpcEndpointsForDomainRequest(BaseModel):
    DomainName: StrictStr
    NextToken: StrictStr | None = None
