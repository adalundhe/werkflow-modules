from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .organizations_handshake import OrganizationsHandshake


class OrganizationsListHandshakesForOrganizationResponse(BaseModel):
    Handshakes: list[OrganizationsHandshake] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
