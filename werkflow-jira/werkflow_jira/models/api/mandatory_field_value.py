from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class MandatoryFieldValue(BaseModel):
    retain: StrictBool | None = None
    type: StrictStr | None = None
    value: list[StrictStr] | None = None
