from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ParameterRemovalDetails(BaseModel):
    parameters: list[StrictStr] | None = None
    schemeId: StrictInt | None = None
    workTypeIds: list[StrictInt] | None = None
