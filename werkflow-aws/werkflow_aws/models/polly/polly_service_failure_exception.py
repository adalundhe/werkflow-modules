from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PollyServiceFailureException(BaseModel):
    message: StrictStr | None = None
