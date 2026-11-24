from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2CustomResponseBody(BaseModel):
    ContentType: StrictStr | None = None
    Content: StrictStr | None = None
