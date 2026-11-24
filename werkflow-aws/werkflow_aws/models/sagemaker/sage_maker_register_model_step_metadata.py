from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerRegisterModelStepMetadata(BaseModel):
    Arn: StrictStr | None = None
