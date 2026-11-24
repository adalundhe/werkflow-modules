from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerUpdateEndpointResponse(BaseModel):
    EndpointArn: StrictStr | None = None
