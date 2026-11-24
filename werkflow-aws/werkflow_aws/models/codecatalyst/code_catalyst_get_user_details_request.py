from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCatalystGetUserDetailsRequest(BaseModel):
    id: StrictStr | None = None
    userName: StrictStr | None = None
