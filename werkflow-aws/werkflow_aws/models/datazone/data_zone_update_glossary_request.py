from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DataZoneUpdateGlossaryRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
    name: StrictStr | None = None
    description: StrictStr | None = None
    status: Literal['DISABLED', 'ENABLED'] | None = None
    clientToken: StrictStr | None = None
