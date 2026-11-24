from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerCreateEndpointConfigResponse(BaseModel):
    EndpointConfigArn: StrictStr | None = None
