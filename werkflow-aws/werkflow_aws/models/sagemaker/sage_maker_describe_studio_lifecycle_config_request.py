from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeStudioLifecycleConfigRequest(BaseModel):
    StudioLifecycleConfigName: StrictStr
