from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerModelDeployResult(BaseModel):
    EndpointName: StrictStr | None = None
