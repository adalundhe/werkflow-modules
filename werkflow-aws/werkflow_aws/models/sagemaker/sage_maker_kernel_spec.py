from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerKernelSpec(BaseModel):
    Name: StrictStr | None = None
    DisplayName: StrictStr | None = None
