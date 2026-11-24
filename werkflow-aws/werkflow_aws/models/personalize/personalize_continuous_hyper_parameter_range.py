from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class PersonalizeContinuousHyperParameterRange(BaseModel):
    name: StrictStr | None = None
    minValue: StrictFloat | StrictInt | None = None
    maxValue: StrictFloat | StrictInt | None = None
