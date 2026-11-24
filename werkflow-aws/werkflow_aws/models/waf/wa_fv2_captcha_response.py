from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class WAFv2CaptchaResponse(BaseModel):
    ResponseCode: StrictInt | None = None
    SolveTimestamp: StrictInt | None = None
    FailureReason: StrictStr | None = None
