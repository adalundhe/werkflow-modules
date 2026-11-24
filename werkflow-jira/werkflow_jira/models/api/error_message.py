from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ErrorMessage(BaseModel):
    message: StrictStr | None = None
