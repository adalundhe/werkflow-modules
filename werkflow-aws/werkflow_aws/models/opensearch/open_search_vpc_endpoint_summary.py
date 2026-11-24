from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchVpcEndpointSummary(BaseModel):
    VpcEndpointId: StrictStr | None = None
    VpcEndpointOwner: StrictStr | None = None
    DomainArn: StrictStr | None = None
    Status: StrictStr | None = None
