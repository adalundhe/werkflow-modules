from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class FMSOrganizationalUnitScope(BaseModel):
    OrganizationalUnits: list[StrictStr] | None = None
    AllOrganizationalUnitsEnabled: StrictBool | None = None
    ExcludeSpecifiedOrganizationalUnits: StrictBool | None = None
