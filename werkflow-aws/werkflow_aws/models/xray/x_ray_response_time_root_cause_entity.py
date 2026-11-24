from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class XRayResponseTimeRootCauseEntity(BaseModel):
    Name: StrictStr | None = None
    Coverage: StrictFloat | StrictInt | None = None
    Remote: StrictBool | None = None
