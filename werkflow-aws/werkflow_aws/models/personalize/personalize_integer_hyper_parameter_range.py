from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class PersonalizeIntegerHyperParameterRange(BaseModel):
    name: StrictStr | None = None
    minValue: StrictInt | None = None
    maxValue: StrictInt | None = None
