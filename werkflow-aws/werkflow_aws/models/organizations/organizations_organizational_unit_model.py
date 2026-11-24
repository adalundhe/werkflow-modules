from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OrganizationsOrganizationalUnitModel(BaseModel):
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    Path: StrictStr | None = None
