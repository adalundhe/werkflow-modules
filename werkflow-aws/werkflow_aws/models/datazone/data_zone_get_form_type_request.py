from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGetFormTypeRequest(BaseModel):
    domainIdentifier: StrictStr
    formTypeIdentifier: StrictStr
    revision: StrictStr | None = None
