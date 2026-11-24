from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SageMakerGlobalInferenceGatewayMemberFilter(BaseModel):
    Name: Literal['Status', 'ClusterArn']
    Value: StrictStr
