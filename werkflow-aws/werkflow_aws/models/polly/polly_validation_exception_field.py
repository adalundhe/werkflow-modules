from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PollyValidationExceptionField(BaseModel):
    name: StrictStr | None = None
    message: StrictStr | None = None
