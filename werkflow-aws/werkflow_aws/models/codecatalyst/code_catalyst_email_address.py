from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CodeCatalystEmailAddress(BaseModel):
    email: StrictStr | None = None
    verified: StrictBool | None = None
