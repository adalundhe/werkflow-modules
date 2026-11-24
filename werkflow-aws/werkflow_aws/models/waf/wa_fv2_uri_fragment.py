from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2UriFragment(BaseModel):
    FallbackBehavior: StrictStr | None = None
