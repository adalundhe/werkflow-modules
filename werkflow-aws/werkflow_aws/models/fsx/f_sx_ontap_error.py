from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxOntapError(BaseModel):
    Message: StrictStr | None = None
    Code: StrictStr | None = None
