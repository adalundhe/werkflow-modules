from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GetCrossProjectReleaseResponse(BaseModel):
    name: StrictStr | None = None
    releaseIds: list[StrictInt] | None = None
