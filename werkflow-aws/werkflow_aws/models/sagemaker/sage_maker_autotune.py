from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAutotune(BaseModel):
    Mode: StrictStr | None = None
