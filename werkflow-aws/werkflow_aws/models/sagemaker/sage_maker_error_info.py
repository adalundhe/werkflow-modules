from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerErrorInfo(BaseModel):
    Code: StrictStr | None = None
    Reason: StrictStr | None = None
