from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchValidationFailure(BaseModel):
    Code: StrictStr | None = None
    Message: StrictStr | None = None
    Severity: StrictStr | None = None
