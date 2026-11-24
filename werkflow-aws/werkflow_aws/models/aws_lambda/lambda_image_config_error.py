from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaImageConfigError(BaseModel):
    ErrorCode: StrictStr | None = None
    Message: StrictStr | None = None
