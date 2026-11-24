from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class ECSResource(BaseModel):
    name: StrictStr | None = None
    type: StrictStr | None = None
    doubleValue: StrictFloat | StrictInt | None = None
    longValue: StrictInt | None = None
    integerValue: StrictInt | None = None
    stringSetValue: list[StrictStr] | None = None
