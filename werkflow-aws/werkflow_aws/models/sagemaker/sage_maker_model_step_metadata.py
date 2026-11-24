from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerModelStepMetadata(BaseModel):
    Arn: StrictStr | None = None
