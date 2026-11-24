from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OrganizationsAcceptHandshakeRequest(BaseModel):
    HandshakeId: StrictStr
