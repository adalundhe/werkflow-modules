from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAddInferenceGatewayRequest(BaseModel):
    Identifier: StrictStr
    ClusterArn: StrictStr
    Namespace: StrictStr
    Name: StrictStr
