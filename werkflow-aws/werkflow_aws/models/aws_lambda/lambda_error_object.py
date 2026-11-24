from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaErrorObject(BaseModel):
    ErrorMessage: StrictStr | None = None
    ErrorType: StrictStr | None = None
    ErrorData: StrictStr | None = None
    StackTrace: list[StrictStr] | None = None
