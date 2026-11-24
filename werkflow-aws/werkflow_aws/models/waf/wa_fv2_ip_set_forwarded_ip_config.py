from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2IPSetForwardedIPConfig(BaseModel):
    HeaderName: StrictStr | None = None
    FallbackBehavior: StrictStr | None = None
    Position: StrictStr | None = None
