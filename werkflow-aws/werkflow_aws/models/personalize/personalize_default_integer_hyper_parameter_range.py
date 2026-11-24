from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class PersonalizeDefaultIntegerHyperParameterRange(BaseModel):
    name: StrictStr | None = None
    minValue: StrictInt | None = None
    maxValue: StrictInt | None = None
    isTunable: StrictBool | None = None
