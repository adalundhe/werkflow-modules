from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaFilterCriteriaError(BaseModel):
    ErrorCode: StrictStr | None = None
    Message: StrictStr | None = None
