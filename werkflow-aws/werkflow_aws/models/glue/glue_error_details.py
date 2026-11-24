from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueErrorDetails(BaseModel):
    ErrorCode: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
