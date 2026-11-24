from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGroupPolicyGrantPrincipal(BaseModel):
    groupIdentifier: StrictStr | None = None
