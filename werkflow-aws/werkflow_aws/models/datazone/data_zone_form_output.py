from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneFormOutput(BaseModel):
    formName: StrictStr | None = None
    typeName: StrictStr | None = None
    typeRevision: StrictStr | None = None
    content: StrictStr | None = None
