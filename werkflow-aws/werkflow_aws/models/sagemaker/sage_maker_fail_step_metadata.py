from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerFailStepMetadata(BaseModel):
    ErrorMessage: StrictStr | None = None
