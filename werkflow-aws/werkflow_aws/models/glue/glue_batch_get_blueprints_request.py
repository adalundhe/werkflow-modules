from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GlueBatchGetBlueprintsRequest(BaseModel):
    Names: list[StrictStr]
    IncludeBlueprint: StrictBool | None = None
    IncludeParameterSpec: StrictBool | None = None
