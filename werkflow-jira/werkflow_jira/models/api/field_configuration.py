from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class FieldConfiguration(BaseModel):
    description: StrictStr | None = None
    id: StrictInt | None = None
    isDefault: StrictBool | None = None
    name: StrictStr | None = None
