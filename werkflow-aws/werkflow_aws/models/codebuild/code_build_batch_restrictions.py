from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CodeBuildBatchRestrictions(BaseModel):
    maximumBuildsAllowed: StrictInt | None = None
    computeTypesAllowed: list[StrictStr] | None = None
    fleetsAllowed: list[StrictStr] | None = None
