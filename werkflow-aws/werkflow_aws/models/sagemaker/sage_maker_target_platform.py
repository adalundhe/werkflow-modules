from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerTargetPlatform(BaseModel):
    Os: StrictStr | None = None
    Arch: StrictStr | None = None
    Accelerator: StrictStr | None = None
