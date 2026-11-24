from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SageMakerGetEndpointPolicyResponse(BaseModel):
    EndpointName: StrictStr | None = None
    EndpointArn: StrictStr | None = None
    ResourcePolicy: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
