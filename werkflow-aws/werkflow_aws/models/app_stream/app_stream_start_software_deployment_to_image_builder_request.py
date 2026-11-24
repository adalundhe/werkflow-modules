from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AppStreamStartSoftwareDeploymentToImageBuilderRequest(BaseModel):
    ImageBuilderName: StrictStr
    RetryFailedDeployments: StrictBool | None = None
