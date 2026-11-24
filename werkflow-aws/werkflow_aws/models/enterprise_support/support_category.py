from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SupportCategory(BaseModel):
    code: StrictStr | None = None
    name: StrictStr | None = None
