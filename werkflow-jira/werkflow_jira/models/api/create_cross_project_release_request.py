from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CreateCrossProjectReleaseRequest(BaseModel):
    name: StrictStr | None = None
    releaseIds: list[StrictInt] | None = None
