from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DataZoneCreateGlossaryRequest(BaseModel):
    domainIdentifier: StrictStr
    name: StrictStr
    owningProjectIdentifier: StrictStr
    description: StrictStr | None = None
    status: Literal['DISABLED', 'ENABLED'] | None = None
    usageRestrictions: list[Literal['ASSET_GOVERNED_TERMS']] | None = None
    clientToken: StrictStr | None = None
