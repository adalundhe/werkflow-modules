from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerEndpointMetadata(BaseModel):
    EndpointName: StrictStr | None = None
    EndpointConfigName: StrictStr | None = None
    EndpointStatus: StrictStr | None = None
    FailureReason: StrictStr | None = None
