from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerInferenceComponentMetadata(BaseModel):
    Arn: StrictStr | None = None
