from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2Regex(BaseModel):
    RegexString: StrictStr | None = None
