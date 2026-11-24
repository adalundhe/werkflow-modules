from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool


class SNSCheckIfPhoneNumberIsOptedOutResponse(BaseModel):
    isOptedOut: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
