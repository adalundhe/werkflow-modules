from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OrganizationsDeclineHandshakeRequest(BaseModel):
    HandshakeId: StrictStr
