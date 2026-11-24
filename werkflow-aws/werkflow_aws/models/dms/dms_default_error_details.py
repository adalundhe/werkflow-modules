from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSDefaultErrorDetails(BaseModel):
    Message: StrictStr | None = None
