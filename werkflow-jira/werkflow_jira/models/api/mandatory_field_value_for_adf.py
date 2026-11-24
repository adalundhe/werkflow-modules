from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class MandatoryFieldValueForADF(BaseModel):
    retain: StrictBool | None = None
    type: StrictStr | None = None
    value: dict[StrictStr, Any] | None = None
