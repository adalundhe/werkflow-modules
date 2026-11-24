from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OrganizationsOrganizationalUnit(BaseModel):
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
