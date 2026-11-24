from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchErrorDetails(BaseModel):
    ErrorType: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
