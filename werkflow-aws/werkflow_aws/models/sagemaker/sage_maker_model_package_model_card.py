from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerModelPackageModelCard(BaseModel):
    ModelCardContent: StrictStr | None = None
    ModelCardStatus: StrictStr | None = None
