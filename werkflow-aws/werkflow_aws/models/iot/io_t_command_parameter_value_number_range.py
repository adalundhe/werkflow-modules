from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTCommandParameterValueNumberRange(BaseModel):
    min: StrictStr | None = None
    max: StrictStr | None = None
