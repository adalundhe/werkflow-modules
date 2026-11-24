from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DirectConnectAsPathSegment(BaseModel):
    pathType: StrictStr | None = None
    path: list[StrictInt] | None = None
