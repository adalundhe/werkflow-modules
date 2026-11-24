from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SageMakerGlobalInferenceGatewayFilter(BaseModel):
    Name: Literal['Status']
    Value: StrictStr
