from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaFunctionCodeLocationError(BaseModel):
    ErrorCode: StrictStr | None = None
    Message: StrictStr | None = None
