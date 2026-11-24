from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SageMakerTrainingSessionModelConfig(BaseModel):
    BaseModelArn: StrictStr | None = None
    AcceptEula: StrictBool | None = None
