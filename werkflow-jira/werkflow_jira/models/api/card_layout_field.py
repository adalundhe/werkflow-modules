from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CardLayoutField(BaseModel):
    fieldId: StrictStr | None = None
    id: StrictInt | None = None
    mode: StrictStr | None = None
    position: StrictInt | None = None
