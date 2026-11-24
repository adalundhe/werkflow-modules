from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AppRunnerDeleteAutoScalingConfigurationRequest(BaseModel):
    AutoScalingConfigurationArn: StrictStr
    DeleteAllRevisions: StrictBool | None = None
