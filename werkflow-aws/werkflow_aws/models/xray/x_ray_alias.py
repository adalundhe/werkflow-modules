from __future__ import annotations
from pydantic import BaseModel, StrictStr


class XRayAlias(BaseModel):
    Name: StrictStr | None = None
    Names: list[StrictStr] | None = None
    Type: StrictStr | None = None
