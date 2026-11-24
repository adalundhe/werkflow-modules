from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueItemError(BaseModel):
    ItemIdentifier: StrictStr | None = None
    Code: StrictStr | None = None
    Message: StrictStr | None = None
