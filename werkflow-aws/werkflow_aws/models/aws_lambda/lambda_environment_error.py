from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaEnvironmentError(BaseModel):
    ErrorCode: StrictStr | None = None
    Message: StrictStr | None = None
