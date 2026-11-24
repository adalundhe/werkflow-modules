from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerVertex(BaseModel):
    Arn: StrictStr | None = None
    Type: StrictStr | None = None
    LineageType: StrictStr | None = None
