from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDirectDeploySettings(BaseModel):
    Status: StrictStr | None = None
