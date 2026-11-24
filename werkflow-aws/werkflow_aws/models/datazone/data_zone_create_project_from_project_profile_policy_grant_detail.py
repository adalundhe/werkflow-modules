from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DataZoneCreateProjectFromProjectProfilePolicyGrantDetail(BaseModel):
    includeChildDomainUnits: StrictBool | None = None
    projectProfiles: list[StrictStr] | None = None
