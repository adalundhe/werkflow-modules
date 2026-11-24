from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTValidationError(BaseModel):
    errorMessage: StrictStr | None = None
