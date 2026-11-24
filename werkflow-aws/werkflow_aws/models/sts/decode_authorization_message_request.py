from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DecodeAuthorizationMessageRequest(BaseModel):
    EncodedMessage: StrictStr | None = None
