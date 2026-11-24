from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightNamespaceError(BaseModel):
    Type: StrictStr | None = None
    Message: StrictStr | None = None
