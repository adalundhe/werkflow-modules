from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMErrorDetails(BaseModel):
    Message: StrictStr | None = None
    Code: StrictStr | None = None
