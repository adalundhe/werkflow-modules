from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DecodeAuthorizationMessageResponse(BaseModel):
    DecodedMessage: StrictStr | None = None
