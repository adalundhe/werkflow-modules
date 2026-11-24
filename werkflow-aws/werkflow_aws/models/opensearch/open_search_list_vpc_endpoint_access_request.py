from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchListVpcEndpointAccessRequest(BaseModel):
    DomainName: StrictStr
    NextToken: StrictStr | None = None
