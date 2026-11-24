from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IssueLinkType(BaseModel):
    id: StrictStr | None = None
    inward: StrictStr | None = None
    name: StrictStr | None = None
    outward: StrictStr | None = None
    self: StrictStr | None = None
