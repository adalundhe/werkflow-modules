from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneFormInput(BaseModel):
    formName: StrictStr
    typeIdentifier: StrictStr | None = None
    typeRevision: StrictStr | None = None
    content: StrictStr | None = None
