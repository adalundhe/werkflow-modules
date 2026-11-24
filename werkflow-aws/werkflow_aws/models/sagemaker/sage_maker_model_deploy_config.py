from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SageMakerModelDeployConfig(BaseModel):
    AutoGenerateEndpointName: StrictBool | None = None
    EndpointName: StrictStr | None = None
