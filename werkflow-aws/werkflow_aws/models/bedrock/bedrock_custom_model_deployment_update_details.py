from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockCustomModelDeploymentUpdateDetails(BaseModel):
    modelArn: StrictStr | None = None
    updateStatus: StrictStr | None = None
