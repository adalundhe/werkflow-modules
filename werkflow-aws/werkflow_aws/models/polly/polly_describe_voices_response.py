from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .polly_voice import PollyVoice


class PollyDescribeVoicesResponse(BaseModel):
    Voices: list[PollyVoice] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
