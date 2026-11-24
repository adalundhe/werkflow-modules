from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OrganizationsHandshakeResource(BaseModel):
    Value: StrictStr | None = None
    Type: StrictStr | None = None
    Resources: list[OrganizationsHandshakeResource] | None = None
