from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2FieldToProtect(BaseModel):
    FieldType: StrictStr | None = None
    FieldKeys: list[StrictStr] | None = None
