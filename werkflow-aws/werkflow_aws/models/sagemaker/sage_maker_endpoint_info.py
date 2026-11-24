from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerEndpointInfo(BaseModel):
    EndpointName: StrictStr | None = None
