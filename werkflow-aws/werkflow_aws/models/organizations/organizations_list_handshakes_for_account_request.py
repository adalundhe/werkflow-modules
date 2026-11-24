from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .organizations_handshake_filter import OrganizationsHandshakeFilter


class OrganizationsListHandshakesForAccountRequest(BaseModel):
    Filter: OrganizationsHandshakeFilter | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
