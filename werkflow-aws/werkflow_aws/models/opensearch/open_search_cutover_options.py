from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchCutoverOptions(BaseModel):
    Target: StrictStr | None = None
    Status: StrictStr | None = None
