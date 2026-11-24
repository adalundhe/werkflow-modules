from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ProjectIdentifiers(BaseModel):
    id: StrictInt | None = None
    key: StrictStr | None = None
    self: StrictStr | None = None
