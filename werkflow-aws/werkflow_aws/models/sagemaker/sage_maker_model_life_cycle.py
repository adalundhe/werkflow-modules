from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerModelLifeCycle(BaseModel):
    Stage: StrictStr | None = None
    StageStatus: StrictStr | None = None
    StageDescription: StrictStr | None = None
