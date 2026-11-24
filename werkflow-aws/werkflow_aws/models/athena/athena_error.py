from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class AthenaError(BaseModel):
    ErrorCategory: StrictInt | None = None
    ErrorType: StrictInt | None = None
    Retryable: StrictBool | None = None
    ErrorMessage: StrictStr | None = None
