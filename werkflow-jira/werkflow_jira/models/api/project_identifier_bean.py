from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ProjectIdentifierBean(BaseModel):
    id: StrictInt | None = None
    key: StrictStr | None = None
