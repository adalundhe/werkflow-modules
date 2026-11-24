from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteStudioLifecycleConfigRequest(BaseModel):
    StudioLifecycleConfigName: StrictStr
