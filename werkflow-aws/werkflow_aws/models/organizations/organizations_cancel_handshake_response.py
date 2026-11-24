from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .organizations_handshake import OrganizationsHandshake


class OrganizationsCancelHandshakeResponse(BaseModel):
    Handshake: OrganizationsHandshake | None = None
    ResponseMetadata: dict[str, Any] | None = None
