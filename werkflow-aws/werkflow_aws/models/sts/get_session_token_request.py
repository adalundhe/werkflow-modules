from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GetSessionTokenRequest(BaseModel):
    DurationSeconds: StrictInt | None = None
    SerialNumber: StrictStr | None = None
    TokenCode: StrictStr | None = None
