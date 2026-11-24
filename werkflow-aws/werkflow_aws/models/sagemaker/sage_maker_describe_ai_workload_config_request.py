from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeAIWorkloadConfigRequest(BaseModel):
    AIWorkloadConfigName: StrictStr
