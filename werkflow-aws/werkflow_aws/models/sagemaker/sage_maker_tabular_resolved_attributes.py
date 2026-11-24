from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerTabularResolvedAttributes(BaseModel):
    ProblemType: StrictStr | None = None
