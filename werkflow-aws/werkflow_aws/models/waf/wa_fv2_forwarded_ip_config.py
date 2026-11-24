from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2ForwardedIPConfig(BaseModel):
    HeaderName: StrictStr | None = None
    FallbackBehavior: StrictStr | None = None
