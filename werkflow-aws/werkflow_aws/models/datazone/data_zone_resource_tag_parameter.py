from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DataZoneResourceTagParameter(BaseModel):
    key: StrictStr | None = None
    value: StrictStr | None = None
    isValueEditable: StrictBool | None = None
