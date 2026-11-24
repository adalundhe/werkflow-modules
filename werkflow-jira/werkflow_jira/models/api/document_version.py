from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DocumentVersion(BaseModel):
    id: StrictStr | None = None
    versionNumber: StrictInt | None = None
