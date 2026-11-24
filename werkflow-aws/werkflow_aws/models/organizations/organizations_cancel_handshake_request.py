from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OrganizationsCancelHandshakeRequest(BaseModel):
    HandshakeId: StrictStr
