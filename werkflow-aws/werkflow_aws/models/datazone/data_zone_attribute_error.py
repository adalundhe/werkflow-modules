from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneAttributeError(BaseModel):
    attributeIdentifier: StrictStr | None = None
    code: StrictStr | None = None
    message: StrictStr | None = None
