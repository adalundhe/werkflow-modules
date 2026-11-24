from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerTextGenerationResolvedAttributes(BaseModel):
    BaseModelName: StrictStr | None = None
