from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeGlobalInferenceGatewayRequest(BaseModel):
    Identifier: StrictStr
