from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteAIWorkloadConfigRequest(BaseModel):
    AIWorkloadConfigName: StrictStr
