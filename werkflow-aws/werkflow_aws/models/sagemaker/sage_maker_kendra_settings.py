from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerKendraSettings(BaseModel):
    Status: StrictStr | None = None
