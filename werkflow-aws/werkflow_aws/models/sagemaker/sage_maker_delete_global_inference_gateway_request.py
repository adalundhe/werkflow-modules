from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteGlobalInferenceGatewayRequest(BaseModel):
    Identifier: StrictStr
