from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OrganizationsChild(BaseModel):
    Id: StrictStr | None = None
    Type: StrictStr | None = None
