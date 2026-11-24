from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class PersonalizeDefaultContinuousHyperParameterRange(BaseModel):
    name: StrictStr | None = None
    minValue: StrictFloat | StrictInt | None = None
    maxValue: StrictFloat | StrictInt | None = None
    isTunable: StrictBool | None = None
